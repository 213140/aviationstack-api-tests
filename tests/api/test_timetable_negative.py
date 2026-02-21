import pytest

pytestmark = [pytest.mark.api, pytest.mark.live]


@pytest.mark.parametrize(
    "iata_code, flight_type",
    [
        ("ABC", "departure"),
        ("JFK", "delay"),
    ],
)
def test_timetable_contract(api_client, iata_code, flight_type):
    params = {
        "iataCode": iata_code,
        "type": flight_type,     
    }

    r = api_client.get_flights_timetable(params=params)
    assert r.status_code == 200

    body = r.json()
    assert "error" in body