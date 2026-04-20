import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


def test_create_student(client):
    data = {
        "name": "John",
        "age": 20,
        "course": "CS"
    }
    response = client.post("/students", json=data)
    assert response.status_code == 200
    assert response.json()["message"] == "Student stored successfully"


def test_get_students(client):
    response = client.get("/students")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
