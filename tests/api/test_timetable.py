import pytest

@pytest.mark.api
@pytest.mark.parametrize(
    "iata_code, flight_type",
    [
        ("JFK", "departure"),
        ("JFK", "arrival"),
    ],
)
def test_timetable_contract(api_client, iata_code, flight_type):
    params = {
        "iataCode": iata_code,
        "type": flight_type,
        "limit": 5      
    }

    r = api_client.get_flights_timetable(params=params)
    assert r.status_code == 200

    body = r.json()
    assert "pagination" in body
    assert "data" in body
    assert isinstance(body["data"], list)
