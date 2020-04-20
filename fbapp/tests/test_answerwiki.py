# coding: utf-8
from fbapp.static.python.answer_wiki import AnswerWiki
import urllib.request
from io import BytesIO
import json
import wikipedia


def test_AnswerWiki_attributs():
    Wiki = AnswerWiki()
    assert type(Wiki.url_answer) == str\
        and type(Wiki.summary_answer) == str and Wiki.wiki_request == []\
        and type(Wiki.text_question) == str and Wiki.keywords == []\
        and Wiki.success is False


def test_wiki_request(monkeypatch):
    results = [
        'Capitole de Toulouse', 'Toulouse 1 University Capitole',
        'Saturnin', 'Courage World Tour', 'Pierre de Fermat',
        'Celine Dion in Concert']

    def mockreturn(request):
        return BytesIO(json.dumps(results).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

    question = AnswerWiki()
    keywords = ['place', 'capitole', 'toulouse']
    ans_page = question._wiki_answer(keywords)
    assert question.wiki_request == 'place capitole toulouse' and\
        ans_page == wikipedia.page('Place du Capitole (Toulouse)')


def test_wiki_parsing():
    question = AnswerWiki()
    text_question = '7 Cité Paradis, 75010 Paris, France'
    question.wiki_parsing(text_question)
    summary = 'La cité Paradis est une voie publique située dans le 10e arrondissement de Paris.\n\n'
    assert question.text_question == '' and\
        question.keywords == ['Cité', 'Paradis', 'Paris', 'France']\
        and question.success is True\
        and question.wiki_request == 'Cité Paradis Paris France' and\
        question.url_answer == "https://fr.wikipedia.org/wiki/Cit%C3%A9_Paradis"\
        and question.summary_answer == summary
