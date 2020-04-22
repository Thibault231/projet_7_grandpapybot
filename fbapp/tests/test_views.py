# coding: utf-8
"""Test views.py module.
"""
import sys
import os
import requests
# Import a new path for pytest
sys.path.append(os.path.abspath(''))
from config import KEYS


def test_connect_website_get():
    """Test the correct connection to the program
    using get request.
    """
    response = requests.get(
        "https://projet-grandpapybot.herokuapp.com")
    assert response.status_code == KEYS['RIGHT_STATUS_TEST']


def test_connection_api_all_post():
    """Test the correct connection to the program
    using post request.
    """
    response = requests.post(
        "https://projet-grandpapybot.herokuapp.com/api/all",
        data={"question": KEYS['TOWN_TEST']})
    assert response.status_code == KEYS['RIGHT_STATUS_TEST']


def test_true_api_all_post():
    """Test the correct response of the program's API
    using a post request with correct datas.
    """
    response = requests.post(
        "https://projet-grandpapybot.herokuapp.com/api/all",
        data={"question": KEYS['TOWN_TEST']})
    file = response.json()
    assert isinstance(file['summary'], str)\
        and file['url'] == 'https://fr.wikipedia.org/wiki/Lyon'\
        and file['adress_ans'] == (
            '{}, France').format(KEYS['TOWN_TEST'])\
        and file['lat_ans'] == KEYS['LAT_TEST']\
        and file['lng_ans'] == KEYS['LNG_TEST']\
        and file['status-code'] == [
            '200-Response complete']\
        and file['success'] is True


def test_empty_api_all_post():
    """Test the correct response of the program's API
    using post request without datas.
    """
    response = requests.post(
        "https://projet-grandpapybot.herokuapp.com/api/all",
        data={"question": ""})
    file = response.json()
    assert file['success'] is False\
        and file['status-code'] == [
            'Error-400-no question']


def test_nokeyword_api_all_post():
    """Test the correct response of the program's API
    using post request with uncorrect datas.
    """
    response = requests.post(
        "https://projet-grandpapybot.herokuapp.com/api/all",
        data={"question": "adresse"})
    file = response.json()
    assert file['success'] is False\
        and file['status-code'] == [
            'Error-400-no keyword in the question']


def test_noplace_api_all_post():
    """Test the correct response of the program's API
    using post request with uncorrect datas.
    """
    response = requests.post(
        "https://projet-grandpapybot.herokuapp.com/api/all",
        data={"question": "sssssqqqqqzzzzz"})
    file = response.json()
    assert file['success'] is False\
        and file['status-code'] == [
            'Error-404-place not found']
