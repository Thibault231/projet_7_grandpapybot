# coding: utf-8
"""[Rule the views of templates and dynamic interractions with them]
"""
import json
from flask import Flask, render_template, request
from fbapp.static.python.answer_wiki import AnswerWiki
from fbapp.static.python.answer_map import AnswerMap
from config import KEYS

APP = Flask(__name__)


@APP.route('/', methods=["GET"])
def index():
    """[Rules the displays of the front side of the web site
    for a 'GET' http-request.]

    Returns:
        index.html [template] -- [templates for user side]
    """
    return render_template('index.html', KEY=KEYS['MAP_KEY'])


@APP.route('/api/all', methods=["POST"])
def api_all():
    """[Rules the API side of the web site
    using a 'POST' http-request. It return usefull informations
    for ajax method in index.html after collecting and cleaning
    datas from Wikipédia's et GoogleMap's APIs]

    Returns:
        response [.json] -- [map and wiki infos]
    """
    if request.method == 'POST':
        print('Connected to API: OK.')
        question_map = AnswerMap()
        question_wiki = AnswerWiki()
        text_question = request.form['question']
        print('Resquest received: OK.')

        if text_question != "":
            print("Question content: OK.")
            question_map.creating_map_infos(text_question)

            if question_map.keywords != []:
                print('Keywords found: OK.')
                if question_map.success:
                    print('GoogleMap response: OK.')
                    question_wiki.wiki_parsing(question_map.adress_answer)

                    if question_wiki.success:
                        print('Wikipedia response: OK.')
                        response = {
                            'summary': question_wiki.summary_answer,
                            'url': question_wiki.url_answer,
                            'adress_ans': question_map.adress_answer,
                            'lat_ans': question_map.lat_answer,
                            'lng_ans': question_map.lng_answer,
                            'success': True,
                            'status-code': '200-Response complete'}
                    else:
                        print('Wikipedia response: Empty.')
                        response = {
                            'success': False,
                            'status-code': 'Error 404-no wikipedia' + \
                                 'page linked to the adress'}

                else:
                    print('GoogleMap response: Error.')
                    response = {
                        'success': False,
                        'status-code': 'Error-404-place not found'}

            else:
                print("Keywords found: None")
                response = {
                    'success': False,
                    'status-code': 'Error-400-no keyword in the question'}
        else:
            print("Question content: empty.")
            response = {
                'success': False,
                'status-code': 'Error-400-no question'}

    response = json.dumps(response)
    return response
