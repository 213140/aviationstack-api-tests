import pytest
from src.api.utils.settings import Settings
from src.api.clients.aviationstack_client import AviationstackClient

@pytest.fixture(scope="session")
def settings() -> Settings:
    return Settings()

@pytest.fixture(scope="session")
def api_client(settings: Settings) -> AviationstackClient:
    api_config = settings.get_api_config()
    return AviationstackClient.from_settings(
        base_url=api_config.base_url,
        access_key=api_config.access_key,
        timeout=api_config.timeout_seconds,
    )


@pytest.fixture
def mock_api_client(api_client, monkeypatch):
    """Return a helper that sets the session.request to always return the provided response."""

    def _set_response(resp):
        def fake_request(method, url, *, params=None, json=None, headers=None, timeout=None, **kwargs):
            return resp

        monkeypatch.setattr(api_client.client.session, "request", fake_request)
        return api_client

    return _set_response
