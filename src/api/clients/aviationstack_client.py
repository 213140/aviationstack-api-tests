from __future__ import annotations
from dataclasses import dataclass
from typing import Any
from src.api.clients.base_client import BaseClient
from typing import Any


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
    
    # Real endpoints, selected two: /aircraft_types and /timetable 
    
    def get_aircraft_types(self, params: dict[str, Any] | None = None):
        return self.client.get("/aircraft_types", params=params)
    
    # Negative test, empty access key
    def get_aircraft_types_negative(self):
        return self.client.get("/aircraft_types", params={"access_key": ""})

    def get_flights_timetable(self, params: dict[str, Any] | None = None):
        return self.client.get("/timetable", params = params)