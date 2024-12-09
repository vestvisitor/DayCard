import pytest
from faker import Faker

from backend.run import app as main_app

faker = Faker("ru_RU")


@pytest.fixture()
def app():
    main_app.config.update(
        {
            "TESTING": True,
        }
    )

    yield main_app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_gel_all_users(client):
    response = client.get("/users/all")
    assert response.status_code == 200


def test_create_existing_user(client):
    response = client.post(
        "/users/signup",
        json={
            "username": "lal",
            "email": "lal",
            "password": "lal",
        }
    )

    assert response.status_code == 409

#
def test_login_and_existing_user(client):
    response = client.post(
        "/users/login",
        json={
            "username": "lal",
            "password": "lal",
        }
    )

    assert response.status_code == 200


def test_login_new_user(client):
    response = client.post(
        "/users/login",
        json={
            "username": "kek",
            "password": "kek",
        }
    )

    assert response.status_code == 409
