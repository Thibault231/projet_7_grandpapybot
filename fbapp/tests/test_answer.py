# coding: utf-8
from fbapp.static.python.answer import Answer


def test_AnswerMap_attributs():
    Quest = Answer()
    assert type(Quest.text_question) == str and Quest.keywords == []\
        and Quest.success is False


def test_create_keywords():
    Quest = Answer()
    text_question = "Salut GrandPy ! Est-ce que tu connais\
         l'adresse d'OpenClassrooms à Paris ?"
    Quest._create_keywords(text_question)
    assert Quest.keywords == ['OpenClassrooms', 'Paris']
