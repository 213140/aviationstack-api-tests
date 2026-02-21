import json
import requests


def make_response(status_code: int, body: dict) -> requests.Response:
    resp = requests.Response()
    resp.status_code = status_code
    resp._content = json.dumps(body).encode("utf-8")
    resp.headers["Content-Type"] = "application/json"
    return resp


def timetable_success(limit: int = 5) -> dict:
    return {
        "pagination": {"limit": limit, "offset": 0, "total": 1},
        "data": [
            {"flight_number": "AB123", "departure": {"icao": "KJFK"}, "arrival": {"icao": "KLAX"}}
        ],
    }


def timetable_error() -> dict:
    return {
        "pagination": {"limit": None, "offset": None, "count": 0, "total": 0},
        "data": {"error": "No Record Found", "success": False},
    }
