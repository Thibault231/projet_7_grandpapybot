# coding: utf-8
from flask import Flask, render_template, request
from fbapp.static.parser import Answer

app = Flask(__name__)
history=[]

@app.route('/', methods=["GET", "POST"])
def index():
    
    if request.method == 'POST':
        question = Answer()
        question.text_question = request.form['text-question']
        history.append(question.text_question)
        question.wiki_parsing()
        question.creating_map_infos()
        return render_template('response.html', summary=question.summary_answer, url=question.url_answer,
         adress_ans=question.adress_answer, lat_ans=question.lat_answer, lng_ans=question.lng_answer,
         history_list=history )
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run()