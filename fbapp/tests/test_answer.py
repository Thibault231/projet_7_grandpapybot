# coding: utf-8
"""Test the Answer.py module.
"""
import sys
import os
sys.path.append(os.path.abspath(''))
from fbapp.static.python.answer import Answer


def test_answermap_attributs():
    """Test the correct creation of Answer's object attributs.
    """
    quest = Answer()
    assert isinstance(quest.text_question, str) and quest.keywords == []\
        and quest.success is False


def test_create_keywords():
    """Test that the function 'create_keywords' transform a string object
    in a list of string objects deleting unsignificant element according
    to a stop_word_list.
    """
    quest = Answer()
    text_question = "Salut GrandPy ! Est-ce que tu connais\
         l'adresse d'OpenClassrooms à Paris ?"
    quest.create_keywords(text_question)
    assert quest.keywords == ['OpenClassrooms', 'Paris']
