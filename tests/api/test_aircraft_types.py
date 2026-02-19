import pytest

@pytest.mark.api
def test_aircraft_types_returns_data_list(api_client):
    r = api_client.get_aircraft_types()
    assert r.status_code == 200

    body = r.json()
    assert "pagination" in body
    assert "data" in body
    assert isinstance(body["data"], list)
