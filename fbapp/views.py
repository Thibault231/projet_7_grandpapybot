# coding: utf-8
"""[Rule the views of templates and dynamic interractions with them]
"""
from flask import Flask, render_template, request
from fbapp.static.parser import Answer

APP = Flask(__name__)
HISTORY = []

@APP.route('/', methods=["GET", "POST"])
def index():
    """[Rules the displays of views depending on
    the requests methods]

    Returns:
        templates [.html] -- [templates for user views]
    """
    if request.method == 'POST':
        question = Answer()
        text_question = request.form['text-question']
        HISTORY.append(text_question)
        question.creating_map_infos(text_question)
        question.wiki_parsing()
        return render_template(
            'response.html', summary=question.summary_answer,
            url=question.url_answer, adress_ans=question.adress_answer,
            lat_ans=question.lat_answer, lng_ans=question.lng_answer,
            history_list=HISTORY)
    else:
        return render_template('index.html')
