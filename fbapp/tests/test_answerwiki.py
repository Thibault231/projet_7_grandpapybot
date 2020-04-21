# coding: utf-8
"""Test the answer_wiki.py module.
"""
import sys
import os
from io import BytesIO
import json
import urllib.request
import wikipedia
sys.path.append(os.path.abspath(''))
from fbapp.static.python.answer_wiki import AnswerWiki


def test_answerwiki_attributs():
    """Test the correct creation of AnswerWiki's object attributs.
    """
    wiki = AnswerWiki()
    assert isinstance(wiki.url_answer, str)\
        and isinstance(wiki.summary_answer, str) and wiki.wiki_request == []\
        and isinstance(wiki.text_question, str) and wiki.keywords == []\
        and wiki.success is False


def test_wiki_request_request(monkeypatch):
    """Test that the function 'wiki_request' once received a list
    of string arguments, transforms it in a simple string element,
    stocked in "wiki_request" attribut.
    This attribut have to be send to wikipedia's API.
    """
    results = [
        'Capitole de Toulouse', 'Toulouse 1 University Capitole',
        'Saturnin', 'Courage World Tour', 'Pierre de Fermat',
        'Celine Dion in Concert']

    def mockreturn():
        return BytesIO(json.dumps(results).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

    question = AnswerWiki()
    keywords = ['place', 'capitole', 'toulouse']
    question.wiki_answer(keywords)
    assert question.wiki_request == 'place capitole toulouse'


def test_wiki_request_ans(monkeypatch):
    """Test that the function 'wiki_request' once send the "wiki_request"
    to wikipedia's API select the first element of the response.
    """
    results = [
        'Capitole de Toulouse', 'Toulouse 1 University Capitole',
        'Saturnin', 'Courage World Tour', 'Pierre de Fermat',
        'Celine Dion in Concert']

    def mockreturn():
        return BytesIO(json.dumps(results).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

    question = AnswerWiki()
    keywords = ['place', 'capitole', 'toulouse']
    ans_page = question.wiki_answer(keywords)
    assert ans_page == wikipedia.page('Place du Capitole (Toulouse)')


def test_wiki_parsing():
    """Test that the function 'wiki_parsing' call Wikipedia API and
    collects summary and wikipedia's url datas in dedicated attributs.
    It must also return the attribute sucess=True.
    """
    question = AnswerWiki()
    text_question = '7 Cité Paradis, 75010 Paris, France'
    question.wiki_parsing(text_question)
    summary = 'La cité Paradis est une voie publique située dans le 10e arrondissement de Paris.'
    assert question.text_question == '' and\
        question.keywords == ['Cité', 'Paradis', 'Paris', 'France']\
        and question.success is True\
        and question.wiki_request == 'Cité Paradis Paris France' and\
        question.url_answer == "https://fr.wikipedia.org/wiki/Cit%C3%A9_Paradis"\
        and question.summary_answer == summary
