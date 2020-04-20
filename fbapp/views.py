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
def all():
    """[Rules the API side of the web site
    using a 'POST' http-request. It return usefull informations
    for ajax method in index.html after collecting and cleaning
    datas from Wikipédia's et GoogleMap's APIs]

    Returns:
        response [.json] -- [map and wiki infos]
    """
    if request.method == 'POST':
        control = []
        print('Connected to API: OK.')
        control.append('Connected to API: OK.//')
        question_map = AnswerMap()
        question_wiki = AnswerWiki()
        text_question = request.form['question']
        print('Resquest received: OK.')
        control.append('Resquest received: OK.//')

        if text_question != "":
            print("Question content: OK.")
            control.append('Question content: OK.//')
            question_map.creating_map_infos(text_question)

            if question_map.success:
                print('GoogleMap response: OK.')
                control.append('GoogleMap response: OK.//')
                question_wiki.wiki_parsing(question_map.adress_answer)

                if question_wiki.success:
                    print('Wikipedia response: OK.')
                    control.append('Wikipedia response: OK.//')
                    response = {
                        'summary': question_wiki.summary_answer,
                        'url': question_wiki.url_answer,
                        'adress_ans': question_map.adress_answer,
                        'lat_ans': question_map.lat_answer,
                        'lng_ans': question_map.lng_answer,
                        'success': True, 'control': control}
                else:
                    print('Wikipedia response: Error.')
                    control.append('Wikipedia response: Error.//')
                    response = {'success': False, 'control': control}

            else:
                print('GoogleMap response: Error.')
                control.append('GoogleMap response: Error.//')
                response = {'success': False, 'control': control}

        else:
            print("Question content: empty.")
            control.append('Question content: empty.//')
            response = {'success': False, 'control': control}

    response = json.dumps(response)
    return response
