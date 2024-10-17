import datetime
import logging
from random import randint
from typing import Dict
from xml.etree.ElementTree import Element

import requests
from lxml import etree
from lxml.html import document_fromstring
from requests import HTTPError, Response

from api_app.analyzers_manager.classes import FileAnalyzer
from api_app.analyzers_manager.exceptions import AnalyzerRunException
from api_app.models import PythonConfig

logger = logging.getLogger(__name__)


class PhishingFormCompiler(FileAnalyzer):
    # good short guide for writing XPath expressions
    # https://upg-dh.newtfire.org/explainXPath.html
    # we're supporting XPath up to v3.1 with elementpath package
    xpath_selector: str
    proxy_address: str = ""

    FAKE_EMAIL_INPUT: str = "fake@email.com"
    FAKE_PASSWORD_INPUT: str = "Fakepassword123!"
    FAKE_TEL_INPUT: str = "+393333333333"

    # mapping between name attribute of text <input>
    # and their corresponding fake values
    _name_text_input_mapping: {tuple: str} = {
        (
            "username",
            "user",
            "name",
            "first-name",
            "last-name",
        ): "fakeuser",  # fake username input
        (
            "card",
            "card_number",
            "card-number",
            "cc",
            "cc-number",
        ): "4111111111111111",  # fake card number input
        ("pin",): "00000",  # fake card pin input
        ("cvv", "cvc"): "000",  # fake card cvc/cvv input
        (
            "exp",
            "date",
            "expiration-date",
            "exp-date",
        ): (datetime.date.today() + datetime.timedelta(days=randint(1, 1000))).strftime(
            "%m/%y"
        ),  # fake random expiration date
    }

    def __init__(
        self,
        config: PythonConfig,
        **kwargs,
    ):
        super().__init__(config, **kwargs)
        self.target_site: str = ""
        self.html_source_code: str = ""
        self.args: [] = []

    def config(self, runtime_configuration: Dict):
        super().config(runtime_configuration)
        if not (hasattr(self._job, "pivot_parent")):
            raise AnalyzerRunException(
                f"Analyzer {self.analyzer_name} must be ran from PhishingAnalysis playbook."
            )

        # extract target site from parent job
        self.target_site = self._job.pivot_parent.starting_job.observable_name
        if self.target_site:
            logger.info(f"Extracted {self.target_site} from parent job")
        else:
            logger.info(
                "Target site from parent job not found! Proceeding with only source code."
            )

        # extract and decode source code from file
        self.html_source_code = self.read_file_bytes()
        if self.html_source_code:
            self.html_source_code = self.html_source_code.decode("utf-8")
            logger.info("Extracted html source code from pivot")
        else:
            raise ValueError("Failed to extract source code from pivot!")

    # @staticmethod
    # def search_phishing_forms_generic(page) -> []:
    #     # extract using standard forms() method
    #     # looking for <form> tags only on HtmlElement type
    #     if isinstance(page, HtmlElement):
    #         return page.forms()
    #
    #     try:
    #         return HtmlElement(page).forms()
    #     except TypeError:
    #         logger.error(f"Page of type {type(page)} can't be converted to HtmlElement")
    #         return []

    @staticmethod
    def search_phishing_forms_xpath(page, xpath_selector: str = "") -> []:
        # extract using a custom XPath selector if set
        return page.xpath(xpath_selector) if xpath_selector else []

    def phishing_forms_exists(self, source: str, xpath_selector: str = "") -> []:
        # recover=True tries to read not well-formed HTML
        html_parser = etree.HTMLParser(recover=True)
        page = document_fromstring(source, parser=html_parser)
        return self.search_phishing_forms_xpath(
            page, xpath_selector
        )  # + search_phishing_forms_generic(page)

    def identify_text_input(self, input_name: str) -> str:
        for names, fake_value in self._name_text_input_mapping.items():
            if input_name in names:
                return fake_value

    def compile_form_field(self, form) -> (dict, str):
        result: {} = {}
        # setting default to page itself if not specified
        if not (form_action := form.get("action", None)):
            form_action = self.target_site
        for element in form.findall(".//input"):
            input_type: str = element.get("type", None)
            input_name: str = element.get("name", None)
            input_value: str = element.get("value", None)
            value_to_set: str = ""
            match input_type.lower():
                case "hidden":
                    logger.info(
                        f"Found hidden input tag with {input_name=} and {input_value=}"
                    )
                    value_to_set = input_value

                case "text":
                    value_to_set = self.identify_text_input(input_name)
                case "password":
                    value_to_set = self.FAKE_PASSWORD_INPUT
                case "tel":
                    value_to_set = self.FAKE_TEL_INPUT
                case "email":
                    value_to_set = self.FAKE_EMAIL_INPUT
                case _:
                    logger.info(f"{input_type.lower()} is not supported yet!")

            logger.info(f"Sending value {value_to_set} for {input_name=}")
            result.setdefault(input_name, value_to_set)
        return result, form_action

    def perform_request_to_form(self, form: Element) -> Response:
        params, dest_url = self.compile_form_field(form)
        logger.info(f"Sending {params=} to submit url {dest_url}")
        return requests.post(
            url=dest_url,
            params=params,
            data=params,
            proxies=(
                {"http": self.proxy_address, "https": self.proxy_address}
                if self.proxy_address
                else None
            ),
        )

    @staticmethod
    def handle_3xx_response(response: Response) -> [str]:
        # extract all redirection history
        return [history.request.url for history in response.history]

    @staticmethod
    def handle_2xx_response(response: Response) -> str:
        return response.request.url

    def analyze_responses(self, responses: [Response]) -> {}:
        result: {str: list} = {"successful": [], "error": []}
        for response in responses:
            try:
                # handle 4xx and 5xx
                response.raise_for_status()
            except HTTPError as e:
                message = f"Error during request to {response.request.url}: {e}"
                logger.error(message)
                result["error"].append(message)
            else:
                if response.history:
                    result["successful"].extend(self.handle_3xx_response(response))

                result["successful"].append(self.handle_2xx_response(response))

        return result

    def run(self) -> dict:
        if not (
            forms := self.phishing_forms_exists(
                self.html_source_code, self.xpath_selector
            )
        ):
            message = (
                f"Form not found in {self.target_site=} with {self.xpath_selector=}! "
                f"Manually check site to see if XPath selector requires some tuning."
            )
            logger.info(message)
            return {"error": message}
        logger.info(f"Found {len(forms)} forms in page {self.target_site}")

        responses: [Response] = []
        for form in forms:
            responses.append(self.perform_request_to_form(form))

        return self.analyze_responses(responses)

    def update(self) -> bool:
        pass
