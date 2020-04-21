# coding: utf-8
"""Test the answer_map.py module.
"""
import sys
import os
import urllib.request
import requests
from io import BytesIO
import json
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

def test_connection_googlemap_api():
    """Test the correct connection to googlemap API
    using the API's Keyword.
    """
    response = requests.get(
            ('https://maps.googleapis.com/maps/api/place/' +
                ('textsearch/json?query={}&key={}').format(
                    "toulouse", KEYS['MAP_KEY']))
            )
    assert response.status_code == 200

def test_google_map_request(monkeypatch):
    """Test that the function 'google_map_request' call GoogleMap API and
    collects lattitude, longitude and adress datas in dedicated attributs.
    """
    results = {
        'results': [{
            'formatted_address': 'Lyon, France',
            'geometry': {
                'location': {
                    'lat': 45.764043,
                    'lng': 4.835659}
                },
            'name': 'Lyon',
            }],
        'status': 'OK'
        }

    def mockreturn():
        return BytesIO(json.dumps(results).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

    question = AnswerMap()
    question.keywords_map = 'lyon'
    question.google_map_request()
    assert question.adress_answer == 'Lyon, France' and\
        question.lat_answer == 45.764043 and\
        question.lng_answer == 4.835659
