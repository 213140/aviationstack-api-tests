import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class ApiConfig:
    name: str
    base_url: str
    access_key: str | None
    timeout_seconds: int


@dataclass(frozen=True)
class Settings:
    default_api_name: str = os.getenv("DEFAULT_API_NAME", "AVIATIONSTACK")

    def get_api_config(self, name: str | None = None) -> ApiConfig:
        api_name = (name or self.default_api_name).upper()

        base_url = os.getenv(f"{api_name}_BASE_URL")
        if not base_url and api_name == "AVIATIONSTACK":
            base_url = os.getenv("API_BASE_URL", "https://api.aviationstack.com/v1")

        access_key = os.getenv(f"{api_name}_ACCESS_KEY")
        if access_key is None and api_name == "AVIATIONSTACK":
            access_key = os.getenv("AVIATIONSTACK_ACCESS_KEY")

        timeout_raw = os.getenv(f"{api_name}_TIMEOUT_SECONDS", os.getenv("TIMEOUT_SECONDS", "10"))
        timeout_seconds = int(timeout_raw)

        if not base_url:
            raise ValueError(f"Missing base URL for API '{api_name}'. Set {api_name}_BASE_URL.")

        return ApiConfig(
            name=api_name,
            base_url=base_url,
            access_key=access_key,
            timeout_seconds=timeout_seconds,
        )
