import pytest
from tests.helpers.mock_responses import make_response, timetable_error

pytestmark = [pytest.mark.api, pytest.mark.mock]


@pytest.mark.parametrize(
    "iata_code, flight_type",
    [
        ("ABC", "departure"),
        ("JFK", "delay"),
    ],
)
def test_timetable_contract(api_client, iata_code, flight_type, mock_api_client):
    params = {
        "iataCode": iata_code,
        "type": flight_type,
    }

    body = timetable_error()
    resp = make_response(200, body)

    # Apply mock and run
    mock_api_client(resp)

    r = api_client.get_flights_timetable(params=params)
    assert r.status_code == 200

    body = r.json()
    assert "data" in body
    assert isinstance(body["data"], dict)
    assert "error" in body["data"]
    assert body["data"].get("success") is False
