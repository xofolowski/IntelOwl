import logging
import os
from typing import Iterator

from selenium.common import WebDriverException
from seleniumbase import Driver
from seleniumbase.config import settings
from seleniumwire.request import Request
from seleniumwire.webdriver import Chrome

# remove annoying driver download message
settings.HIDE_DRIVER_DOWNLOADS = True

LOG_NAME = "driver_wrapper"

# get flask-shell2http logger instance
logger = logging.getLogger(LOG_NAME)
# logger config
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
log_level = os.getenv("LOG_LEVEL", logging.INFO)
log_path = os.getenv("LOG_PATH", f"/var/log/intel_owl/{LOG_NAME}")
# create new file handlers, files are created if doesn't already exists
fh = logging.FileHandler(f"{log_path}/{LOG_NAME}.log")
fh.setFormatter(formatter)
fh.setLevel(log_level)
fh_err = logging.FileHandler(f"{log_path}/{LOG_NAME}_errors.log")
fh_err.setFormatter(formatter)
fh_err.setLevel(logging.ERROR)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(fh_err)
logger.setLevel(log_level)


class DriverWrapper:
    def __init__(self, proxy_address: str = ""):
        self.proxy: str = proxy_address
        self.driver: Chrome = self._init_driver()
        self.last_url: str = ""

    def _init_driver(self) -> Chrome:
        logger.info(f"Adding proxy with option: {self.proxy}")
        logger.info("Creating Chrome driver...")
        # no_sandbox=True sucks but it's almost the only way to run chromium-based
        # browsers in docker. browser is running as unprivileged user and
        # it's in a container: trade-off
        driver = Driver(
            headless=True,
            headless2=True,
            use_wire=True,
            no_sandbox=True,
            proxy=self.proxy or None,
            proxy_bypass_list=self.proxy or None,
            browser="chrome",
        )
        # TODO: make window size a parameter
        driver.set_window_size(1920, 1080)
        return driver

    def restart(self, motivation: str = ""):
        logger.info(f"Restarting driver: {motivation}")
        self.driver.quit()
        self.driver = self._init_driver()
        if self.last_url:
            self.navigate(self.last_url)

    def navigate(self, url: str):
        if not url:
            logger.error("Empty URL! Something's wrong!")
            return

        self.last_url = url
        try:
            self.driver.get(url)
        except WebDriverException as e:
            logger.error("navigate")
            logger.error(e)
            self.restart(motivation="navigate")

    @property
    def page_source(self) -> str:
        try:
            return self.driver.page_source
        except WebDriverException as e:
            logger.error("page_source")
            logger.error(e)
            self.restart(motivation="page_source")
            return self.page_source

    @property
    def current_url(self) -> str:
        try:
            return self.driver.current_url
        except WebDriverException as e:
            logger.error("current_url")
            logger.error(e)
            self.restart(motivation="current_url")
            return self.current_url

    @property
    def base64_screenshot(self) -> str:
        try:
            return self.driver.get_screenshot_as_base64()
        except WebDriverException as e:
            logger.error("base64_screenshot")
            logger.error(e)
            self.restart(motivation="base64_screenshot")
            return self.base64_screenshot

    def iter_requests(self) -> Iterator[Request]:
        return self.driver.iter_requests()

    def quit(self):
        self.driver.quit()