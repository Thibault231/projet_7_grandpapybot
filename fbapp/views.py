# coding: utf-8
"""[Rule the views of templates and dynamic interractions with them]
"""
import json
from flask import Flask, render_template, request
from fbapp.static.python.answer_wiki import AnswerWiki
from fbapp.static.python.answer_map import AnswerMap
from fbapp.static.python.answer import Answer
from config import KEYS

APP = Flask(__name__)

@APP.route('/', methods=["GET"])
def index():
    """[Rules the displays of the front side of the web site
    for a 'GET' http-request.]

    Returns:
        index.html [template] -- [templates for user side]
    """
    return render_template('index.html', KEY= KEYS['MAP_KEY'])

@APP.route('/api/all', methods=["POST"])
def all():
    """[Rules the API side of the web site
    using a 'POST' http-request. It return usefull informations
    for ajax method in index.html after collecting and cleaning
    datas from Wikipédia's et GoogleMap's APIs]

    Returns:
        response [.json] -- [map and wiki infos]
    """
    if request.method == 'POST':
        question_map = AnswerMap()
        question_wiki = AnswerWiki()
        text_question = request.form['question']
        question_map.creating_map_infos(text_question)
        if question_map.success:
            question_wiki.wiki_parsing(question_map.adress_answer)
            if question_wiki.success:
                response = {'summary': question_wiki.summary_answer,
                'url': question_wiki.url_answer, 'adress_ans': question_map.adress_answer,
                'lat_ans': question_map.lat_answer, 'lng_ans': question_map.lng_answer,
                'success': True}
        else:
            response = {'success': False}
        
        response = json.dumps(response)
        return  response 
        
@APP.route('/api/wiki', methods=["POST"])
def wiki():
    """[Rules the API side of the web site
    for a 'POST' http-request. It return wikipédia informations
    about the request after collecting and cleaning datas from
    Wikipédia's API.]

    Returns:
        response [.json] -- [wiki infos]
    """
    if request.method == 'POST':
        question = AnswerWiki()
        self.text_question = request.form['text-question']
        question.wiki_parsing(self.text_question)

        if question_wiki.success:
            response = {'summary': question.summary_answer,
                'url': question.url_answer,'success': True}
        else:
            response = {'success': False}
        
        response = json.dumps(response)
        return  response

@APP.route('/api/map', methods=["POST"])
def map():
    """[Rules the API side of the web site
    for a 'POST' http-request. It return wikipédia informations
    about the request after collecting and cleaning datas from
    GoogleMap's API.]

    Returns:
        response [.json] -- [géographical infos]
    """
    if request.method == 'POST':
        question = AnswerMap()
        text_question = request.form['question']
        question.creating_map_infos(text_question)

        if question_map.success:
            response = {'adress_ans': question.adress_answer,
                'lat_ans': question.lat_answer, 'lng_ans': question.lng_answer,
                'success': True}
        else:
            response = {'success': False}
        
        response = json.dumps(response)
        return  response

if __name__ == "__main__":
   a = AnswerWiki()