from __future__ import annotations
from dataclasses import dataclass
from typing import Any
from urllib.parse import urljoin
import requests


@dataclass
class BaseClient:
    base_url: str
    timeout: int = 10
    default_params: dict[str, Any] | None = None

    def __post_init__(self) -> None:
        self.session = requests.Session()

    def _url(self, path: str) -> str:
        return urljoin(self.base_url.rstrip("/") + "/", path.lstrip("/"))

    def request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> requests.Response:
        final_params: dict[str, Any] = {}
        if self.default_params:
            final_params.update(self.default_params)
        if params:
            final_params.update(params)

        response = self.session.request(
            method=method.upper(),
            url=self._url(path),
            params=final_params if final_params else None,
            json=json,
            headers=headers,
            timeout=self.timeout,
        )
        return response

    def get(self, path: str, *, params: dict[str, Any] | None = None) -> requests.Response:
        return self.request("GET", path, params=params)
