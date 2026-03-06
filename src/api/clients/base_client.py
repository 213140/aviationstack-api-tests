from __future__ import annotations
from dataclasses import dataclass
from typing import Any
from urllib.parse import urljoin
import logging
import time
import uuid
import requests


@dataclass
class BaseClient:
    base_url: str
    timeout: int = 10
    default_params: dict[str, Any] | None = None

    def __post_init__(self) -> None:
        self.session = requests.Session()
        self.logger = logging.getLogger("api.client")

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

        request_id = uuid.uuid4().hex[:8]
        start_time = time.perf_counter()

        safe_params = dict(final_params) if final_params else None
        if safe_params and "access_key" in safe_params:
            safe_params["access_key"] = "***"

        self.logger.info(
            "request_id=%s method=%s url=%s params=%s",
            request_id,
            method.upper(),
            self._url(path),
            safe_params,
        )

        try:
            response = self.session.request(
                method=method.upper(),
                url=self._url(path),
                params=final_params if final_params else None,
                json=json,
                headers=headers,
                timeout=self.timeout,
            )
        except requests.RequestException:
            elapsed_ms = (time.perf_counter() - start_time) * 1000
            self.logger.exception(
                "request_id=%s failed after %.2fms",
                request_id,
                elapsed_ms,
            )
            raise

        elapsed_ms = (time.perf_counter() - start_time) * 1000
        self.logger.info(
            "request_id=%s status=%s elapsed_ms=%.2f",
            request_id,
            response.status_code,
            elapsed_ms,
        )
        return response

    def get(self, path: str, *, params: dict[str, Any] | None = None) -> requests.Response:
        return self.request("GET", path, params=params)
