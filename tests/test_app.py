"""Integration Test with dockerized db"""
import pytest
from fastapi.testclient import TestClient

from be.app import app


@pytest.fixture
def api_client():
    return TestClient(app)


def test_create_waypoint_valid(api_client):
    res = api_client.post("/waypoints/", json={"waypoint": "2.43, 12.0"})
    assert res.status_code == 201
    data = res.json()
    assert data["latitude"] == 2.43
    assert data["longitude"] == 12.0


def test_create_waypoint_coordinates_out_of_bounds(api_client):
    res = api_client.post("/waypoints/", json={"waypoint": "200.43, 200.0"})
    assert res.status_code == 422


def test_create_waypoint_coordinates_invalid(api_client):
    res = api_client.post("/waypoints/", json={"waypoint": "foo bar"})
    assert res.status_code == 422


def test_read_paged_waypoints(api_client):
    res = api_client.get("/waypoints?offset=0&limit=10")

    assert res.ok
    data = res.json()
    assert len(data["values"]) == 10
