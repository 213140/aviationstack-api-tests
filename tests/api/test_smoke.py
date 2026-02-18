import pytest

@pytest.mark.api
def test_client_is_configured(api_client):
    assert api_client is not None # Checking if client exists
