from __future__ import annotations
from dataclasses import dataclass
from typing import Any
from src.api.clients.base_client import BaseClient


@dataclass
class AviationstackClient:
    client: BaseClient

    @classmethod
    def from_settings(cls, base_url: str, access_key: str | None, timeout: int) -> "AviationstackClient":
        default_params: dict[str, Any] = {}
        if access_key:
            default_params["access_key"] = access_key

        base = BaseClient(base_url=base_url, timeout=timeout, default_params=default_params)
        return cls(client=base)

    # will be replaced by real endpoint call
    def get_raw(self, path: str, params: dict[str, Any] | None = None):
        return self.client.get(path, params=params) 
