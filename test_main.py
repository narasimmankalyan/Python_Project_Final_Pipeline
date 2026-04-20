from fastapi.testclient import TestClient
 
from main import app

client = TestClient(app)



def test_create_student():
    data = {
        "name": "John",
        "age": 20,
        "course": "CS"
    }
    response = client.post("/students", json=data)
    assert response.status_code == 200
    assert response.json()["message"] == "Student stored successfully"


def test_get_students():
    response = client.get("/students")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
