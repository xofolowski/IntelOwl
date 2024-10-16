import base64
import logging
from typing import Dict

from api_app.analyzers_manager.classes import DockerBasedAnalyzer, FileAnalyzer
from api_app.analyzers_manager.exceptions import AnalyzerRunException
from api_app.models import PythonConfig

logger = logging.getLogger(__name__)


class PhishingFormCompiler(FileAnalyzer, DockerBasedAnalyzer):
    name: str = "Phishing_Form_Compiler"
    url: str = "http://phishing_analyzers:4005/phishing_form_compiler"
    max_tries: int = 20
    poll_distance: int = 3

    # good short guide for writing XPath expressions
    # https://upg-dh.newtfire.org/explainXPath.html
    # we're supporting XPath up to v3.1 with elementpath package
    xpath_selector: str
    proxy_protocol: str = ""
    proxy_address: str = ""
    proxy_port: int = 0

    def __init__(
        self,
        config: PythonConfig,
        **kwargs,
    ):
        super().__init__(config, **kwargs)
        self.target_site: str = ""
        self.html_source_code: bytes = b""
        self.args: [] = []

    def config(self, runtime_configuration: Dict):
        super().config(runtime_configuration)

        if not (hasattr(self._job, "pivot_parent")):
            raise AnalyzerRunException(
                f"Analyzer {self.analyzer_name} must be ran from PhishingAnalysis playbook."
            )

        self.target_site = self._job.pivot_parent.starting_job.observable_name
        if self.target_site:
            logger.info(f"Extracted {self.target_site} from parent job")
        else:
            logger.info(
                "Target site from parent job not found! Proceeding with only source code."
            )

        if self.proxy_address:
            self.args.append(f"--proxy_address={self.proxy_address}")
            if self.proxy_protocol:
                self.args.append(f"--proxy_protocol={self.proxy_protocol}")
            if self.proxy_port:
                self.args.append(f"--proxy_port={self.proxy_port}")

        self.html_source_code = self.read_file_bytes()

    def run(self) -> dict:
        req_data: {} = {
            "args": [
                f"--target_site={self.target_site}",
                f"--source_code={base64.b64encode(self.html_source_code).decode('utf-8')}",
                f"--xpath_selector={self.xpath_selector}",
                *self.args,
            ]
        }
        logger.info(f"sending {req_data=} to {self.url}")
        return self._docker_run(req_data)

    def update(self) -> bool:
        pass
