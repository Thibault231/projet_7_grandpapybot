# coding: utf-8
from fbapp.static.python.answer_map import AnswerMap
import urllib.request
from io import BytesIO
import json


def test_AnswerMap_attributs():
    Map = AnswerMap()
    assert type(Map.keywords_map) == str and type(Map.adress_answer) == str\
        and type(Map.lat_answer) == float and type(Map.lng_answer) == float\
        and type(Map.text_question) == str and Map.keywords == []\
        and Map.success is False


def test_google_map_request(monkeypatch):
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

    def mockreturn(request):
        return BytesIO(json.dumps(results).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

    question = AnswerMap()
    question.keywords_map = 'lyon'
    question._google_map_request()
    assert question.adress_answer == 'Lyon, France' and\
        question.lat_answer == 45.764043 and\
        question.lng_answer == 4.835659
