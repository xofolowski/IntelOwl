import json
import logging

from knock.knockpy import KNOCKPY

from api_app.analyzers_manager import classes
from tests.mock_utils import MockUpResponse, if_mock_connections, patch

logger = logging.getLogger(__name__)


class KnockAnalyzer(classes.ObservableAnalyzer):
    """
    This analyzer is a wrapper for the knockpy project.
    """

    observable_name: str
    dns: str = None
    useragent: str = None
    timeout: int = None
    threads: int = None
    recon: bool = True
    bruteforce: bool = True

    def update(self) -> bool:
        pass

    def run(self):
        logger.info(f"Running KnockAnalyzer for {self.observable_name}")
        results = KNOCKPY(
            domain=self.observable_name,
            dns=self.dns,
            useragent=self.useragent,
            timeout=self.timeout,
            threads=self.threads,
            recon=self.recon,
            bruteforce=self.bruteforce,
        )

        return json.dumps(results)

    @classmethod
    def _monkeypatch(cls):
        patches = [
            if_mock_connections(
                patch(
                    "requests.get",
                    return_value=MockUpResponse(
                        {
                            "malektravel.domain.com": ["66.96.162.92"],
                            "http": [403, None, "Apache"],
                            "https": [403, None, "Apache"],
                            "cert": [True, "2024-10-08"],
                        },
                        {
                            "mchattan01.domain.com": ["66.96.162.92"],
                            "http": [200, None, "Apache"],
                            "https": [None, None, None],
                            "cert": [None, None],
                        },
                        {
                            "martina6marco.domain.com": ["66.96.162.92"],
                            "http": [500, None, "Apache"],
                            "https": [None, None, None],
                            "cert": [None, None],
                        },
                        {
                            "maludomaincom.domain.com": ["66.96.162.92"],
                            "http": [403, None, "Apache"],
                            "https": [403, None, "Apache"],
                            "cert": [True, "2024-10-08"],
                        },
                        {
                            "margaretlion.domain.com": ["66.96.162.92"],
                            "http": [200, None, "Apache"],
                            "https": [200, None, "Apache"],
                            "cert": [True, "2024-10-08"],
                        },
                        200,
                    ),
                )
            )
        ]
        return super()._monkeypatch(patches=patches)
