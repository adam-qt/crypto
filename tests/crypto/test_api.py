import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


def get_data_for_crypto():
    crypto_data = {
        "name": "Crypto 1",
        "slug": "crypto-1",
        "total_supply": 11,
        "price": 12,
        "market_cap": 2323,
        "volume_change_24h": 11.1,
        "percent_change_24h": 11.1,
        "user_favourite": "",
    }
    return crypto_data


@pytest.mark.django_db
def test_crypto_list():
    client = APIClient()
    response = client.get("/API/crypto/")
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_crypto_create_bad_request():
    client = APIClient()
    crypto_data = get_data_for_crypto()
    response = client.post("/API/crypto/", data=crypto_data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_crypto_create_exists():
    client = APIClient()
    user = User.objects.create_user(username="usernname_1", password="password12")
    crypto_data = get_data_for_crypto()
    crypto_data["user_favourite"] = user.pk
    response = client.post("/API/crypto/", data=crypto_data)
    response = client.post("/API/crypto/", data=crypto_data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_crypto_create():
    client = APIClient()
    user = User.objects.create_user(username="usernname_1", password="password12")
    crypto_data = get_data_for_crypto()
    crypto_data["user_favourite"] = user.pk
    response = client.post("/API/crypto/", data=crypto_data)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_crypto_detail_not_found():
    client = APIClient()
    user = User.objects.create_user(username="usernname_1", password="password12")
    crypto_data = get_data_for_crypto()
    crypto_data["user_favourite"] = user.pk
    response = client.post("/API/crypto/", data=crypto_data)
    slug_search = "asa"
    response = client.get(f"/API/crypto/{slug_search}/")
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_crypto_detail():
    client = APIClient()
    user = User.objects.create_user(username="usernname_1", password="password12")
    crypto_data = get_data_for_crypto()
    crypto_data["user_favourite"] = user.pk
    response = client.post("/API/crypto/", data=crypto_data)
    slug_search = crypto_data["slug"]
    response = client.get(f"/API/crypto/{slug_search}/")
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_crypto_update_not_found():
    client = APIClient()
    user = User.objects.create_user(username="usernname_1", password="password12")
    crypto_data = get_data_for_crypto()
    crypto_data["user_favourite"] = user.pk
    crypto_data["name"] = "Crypto 23"
    response = client.post("/API/crypto/", data=crypto_data)
    slug_search = "slug"
    response = client.put(f"/API/crypto/{slug_search}/")
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_crypto_update():
    client = APIClient()
    user = User.objects.create_user(username="usernname_1", password="password12")
    crypto_data = get_data_for_crypto()
    crypto_data["user_favourite"] = user.pk
    crypto_data["name"] = "Crypto new name"
    response = client.post("/API/crypto/", data=crypto_data)
    slug_search = crypto_data["slug"]
    response = client.put(f"/API/crypto/{slug_search}/", data=crypto_data)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_crypto_delete_not_found():
    client = APIClient()
    user = User.objects.create_user(username="usernname_1", password="password12")
    crypto_data = get_data_for_crypto()
    crypto_data["user_favourite"] = user.pk
    crypto_data["name"] = "Crypto 23"
    response = client.post("/API/crypto/", data=crypto_data)
    slug_search = "slug"
    response = client.delete(f"/API/crypto/{slug_search}/")
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_crypto_delete():
    client = APIClient()
    user = User.objects.create_user(username="usernname_1", password="password12")
    crypto_data = get_data_for_crypto()
    crypto_data["user_favourite"] = user.pk
    response = client.post("/API/crypto/", data=crypto_data)
    slug_search = crypto_data["slug"]
    response = client.delete(f"/API/crypto/{slug_search}/")
    assert response.status_code == status.HTTP_204_NO_CONTENT
