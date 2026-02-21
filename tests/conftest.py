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


@pytest.fixture
def mock_api_client(api_client, monkeypatch):
    """Return a helper that sets the session.request to always return the provided response."""

    def _set_response(resp):
        def fake_request(method, url, *, params=None, json=None, headers=None, timeout=None, **kwargs):
            return resp

        monkeypatch.setattr(api_client.client.session, "request", fake_request)
        return api_client

    return _set_response
