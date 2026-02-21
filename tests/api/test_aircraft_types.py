import pytest
from jsonschema import validate


@pytest.mark.api
def test_aircraft_types_returns_data_list(api_client):
    r = api_client.get_aircraft_types()
    assert r.status_code == 200

    body = r.json()
    assert "pagination" in body
    assert "data" in body
    assert isinstance(body["data"], list)

    # JSON Schema for /aircraft_types positive response (minimal contract)
    schema = {
        "type": "object",
        "required": ["pagination", "data"],
        "properties": {
            "pagination": {
                "type": "object",
                "properties": {
                    "limit": {"type": ["integer", "null"]},
                    "offset": {"type": ["integer", "null"]},
                    "total": {"type": ["integer", "null"]},
                    "count": {"type": ["integer", "null"]},
                },
            },
            "data": {
                "type": "array",
                "items": {"type": "object"},
            },
        },
    }

    validate(instance=body, schema=schema)
