import pytest
from src.api.utils.settings import Settings
from src.api.clients.aviationstack_client import AviationstackClient

@pytest.fixture(scope="session")
def settings() -> Settings:
    return Settings()

@pytest.fixture(scope="session")
def api_client(settings: Settings) -> AviationstackClient:
    return AviationstackClient.from_settings(
        base_url=settings.base_url,
        access_key=settings.access_key,
        timeout=settings.timeout_seconds,
    )
