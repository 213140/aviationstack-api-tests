import pytest
from tests.helpers.mock_responses import make_response, timetable_success

pytestmark = [pytest.mark.api, pytest.mark.mock]


@pytest.mark.parametrize(
    "iata_code, flight_type",
    [
        ("JFK", "departure"),
        ("JFK", "arrival"),
    ],
)
def test_timetable_contract(api_client, iata_code, flight_type, mock_api_client):
    params = {
        "iataCode": iata_code,
        "type": flight_type,
        "limit": 5,
    }

    body = timetable_success(limit=5)
    resp = make_response(200, body)

    # Apply mock and run
    mock_api_client(resp)

    r = api_client.get_flights_timetable(params=params)
    assert r.status_code == 200

    body = r.json()
    assert "pagination" in body
    assert "data" in body
    assert isinstance(body["data"], list)
