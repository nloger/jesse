from fastapi.testclient import TestClient
from jesse.services.web import fastapi_app
from hashlib import sha256

client = TestClient(fastapi_app)


def test_home_route():
    response = client.get("/")
    assert response.status_code == 200


def test_auth_end_point():
    # password set's to password for tests
    # first check wrong password
    response = client.post(
        '/auth',
        json={"password": "some"}
    )
    assert response.status_code == 401
    assert response.json() == {
        'message': 'Invalid password'
    }
    # now check correct password
    response = client.post(
        '/auth',
        json={"password": "password"}
    )
    assert response.status_code == 200
    assert response.json() == {
        'auth_token': sha256('password'.encode('utf-8')).hexdigest()
    }
