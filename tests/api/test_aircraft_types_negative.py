import pytest

@pytest.mark.api
def test_aircraft_types_negative(api_client):
    r = api_client.get_aircraft_types_negative()
    assert r.status_code == 401

    body = r.json()
    assert "error" in body