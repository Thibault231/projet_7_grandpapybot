# coding: utf-8
"""Test the answer_map.py module.
"""
import sys
import os
import urllib.request
import json
from io import BytesIO
import requests
# Import a new path for pytest
sys.path.append(os.path.abspath(''))
from fbapp.static.python.answer_map import AnswerMap
from config import KEYS


def test_answermap_attributs():
    """Test the correct creation of AnswerMap's object attributs.
    """
    map1 = AnswerMap()
    assert isinstance(map1.keywords_map, str) and\
        isinstance(map1.adress_answer, str) and\
        isinstance(map1.lat_answer, float) and\
        isinstance(map1.lng_answer, float) and\
        isinstance(map1.text_question, str) and map1.keywords == [] and\
        map1.success is False


def test_right_connection_googlemap_api():
    """Test the correct connection to googlemap API
    using the API's Keyword. Check that adress et geopraphical
    datas are return in the results.
    """
    response = requests.get(
        ('https://maps.googleapis.com/maps/api/place/' +
         ('textsearch/json?query={}&key={}').format(
             KEYS['TOWN_TEST'], KEYS['MAP_KEY'])))
    file = response.json()
    assert response.status_code == KEYS['RIGHT_STATUS_TEST']\
        and isinstance(
            file['results'][0]['formatted_address'], str)\
        and isinstance(
            file['results'][0]['geometry']['location']['lat'], float)\
        and isinstance(
            file['results'][0]['geometry']['location']['lng'], float)


def test_wrong_connection_googlemap_api():
    """Test the connection to googlemap API
    using wrong Keyword.
    """
    response = requests.get(
        ('https://maps.googleapis.com/maps/api/place/' +
         ('textsearch/json?query={}&key={}').format(
             'sssssfffff11111', KEYS['MAP_KEY'])))
    assert response.status_code == KEYS['RIGHT_STATUS_TEST']\
        and isinstance(response.content, bytes)


def test_google_map_request(monkeypatch):
    """Test that the function 'google_map_request' call GoogleMap API and
    collects lattitude, longitude and adress datas in dedicated attributs.
    """
    results = {
        'results': [{
            'formatted_address': ('{}, France').format(KEYS['TOWN_TEST']),
            'geometry': {
                'location': {
                    'lat': KEYS['LAT_TEST'],
                    'lng': KEYS['LNG_TEST']}
                },
            'name': KEYS['TOWN_TEST'],
            }],
        'status': 'OK'
        }

    def mockreturn():
        return BytesIO(json.dumps(results).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

    question = AnswerMap()
    question.keywords_map = KEYS['TOWN_TEST']
    question.google_map_request()
    assert question.adress_answer == ('{}, France').format(
        KEYS['TOWN_TEST']) and\
        question.lat_answer == KEYS['LAT_TEST'] and\
        question.lng_answer == KEYS['LNG_TEST']
