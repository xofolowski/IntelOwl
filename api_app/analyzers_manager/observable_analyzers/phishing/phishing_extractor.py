from logging import getLogger
from typing import Dict

from api_app.analyzers_manager.classes import DockerBasedAnalyzer, ObservableAnalyzer
from api_app.models import PythonConfig

logger = getLogger(__name__)


class PhishingExtractor(ObservableAnalyzer, DockerBasedAnalyzer):
    name: str = "Phishing_Extractor"
    url: str = "http://phishing_analyzers:4005/phishing_extractor"
    max_tries: int = 20
    poll_distance: int = 3

    proxy_address: str = ""

    def __init__(
        self,
        config: PythonConfig,
        **kwargs,
    ):
        super().__init__(config, **kwargs)
        self.args: [] = []

    def config(self, runtime_configuration: Dict):
        super().config(runtime_configuration)
        self.args.append(f"--target={self.observable_name}")
        if self.proxy_address:
            self.args.append(f"--proxy_address={self.proxy_address}")

    def run(self):
        req_data: {} = {
            "args": [
                *self.args,
            ],
        }
        logger.info(f"sending {req_data=} to {self.url}")
        return self._docker_run(req_data)

    def update(self) -> bool:
        pass