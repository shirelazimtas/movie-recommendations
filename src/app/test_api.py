from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_get_movies():
    response = client.get("/v1/batmen")
    assert response.status_code == 200


def test_get_genres():
    response = client.get("/v2/Comedy")
    assert response.status_code == 200


def test_get_wikipedia():
    response = client.get("/v3/comedyfilm")
    assert response.status_code == 200
