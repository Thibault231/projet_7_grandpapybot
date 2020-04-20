# coding: utf-8
import requests


def test_connect_api_all_post():
    response = requests.get(
        "https://projet-grandpapybot.herokuapp.com")
    assert response.status_code == 200


def test_true_api_all_post():
    a = requests.post(
        "https://projet-grandpapybot.herokuapp.com/api/all",
        data={"question": "openclassrooms"})
    file = a.json()
    summary = 'La cité Paradis est une voie publique située\
         dans le 10e arrondissement de Paris.\n\n'
    assert file['summary'] == summary\
        and file['url'] == 'https://fr.wikipedia.org/wiki/Cit%C3%A9_Paradis'\
        and file['adress_ans'] == '7 Cité Paradis, 75010 Paris, France'\
        and file['lat_ans'] == 48.8748465\
        and file['lng_ans'] == 2.3504873\
        and file['control'] == [
            'Connected to API: OK.//', 'Resquest received: OK.//',
            'Question content: OK.//', 'GoogleMap response: OK.//',
            'Wikipedia response: OK.//']\
        and file['success'] is True


def test_empty_api_all_post():
    a = requests.post(
        "https://projet-grandpapybot.herokuapp.com/api/all",
        data={"question": ""})
    file = a.json()
    assert file['success'] is False\
        and file['control'] == [
         'Connected to API: OK.//',
         'Resquest received: OK.//',
         'Question content: empty.//']


def test_wrong_api_all_post():
    a = requests.post(
        "https://projet-grandpapybot.herokuapp.com/api/all",
        data={"question": "sssssqqqqqzzzzz"})
    file = a.json()
    assert file['success'] is False\
        and file['control'] == [
            'Connected to API: OK.//',
            'Resquest received: OK.//',
            'Question content: OK.//',
            'GoogleMap response: Error.//']
