# testas kuris tikrins 2 argumentu suma
import mock

from pythonProject6.main import two_numbers_addition
from pythonProject6.main import numbers_substraction
from pythonProject6.main import any_function
import pytest
import requests


@mock.patch("requests.get")
def test_website_response(mock_get):
    mock_get.return_value.status_code = 200
    response = requests.get("http://www.google.lt/mock")
    assert response.status_code == 200


def test_website_response_no_mock():

    response = requests.get("http://www.google.lt/mock")
    assert response.status_code == 404


def test_any_function():
    assert any_function() == "anything"


@pytest.fixture()
def add_ten():
    return 10


def test_two_numbers_addition(add_ten):
    assert two_numbers_addition(1, add_ten) == 11


def test_number_substraction():
    assert numbers_substraction(7, 8) == -1

def test_selector_number_substraction():
    assert numbers_substraction(7, 8) == -1




























""""""
# pip install coverage
# coverage run --source="." --omit="*/venv/*" -m pytest
# coverage report main.py
# coverage html main.py