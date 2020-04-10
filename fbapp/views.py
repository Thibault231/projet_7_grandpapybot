# coding: utf-8
from flask import Flask, render_template, request
from fbapp.static.parser import wiki_parsing, creating_map_infos


app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        MAP_KEY = "AIzaSyA63EmB7d3J1w_6axs28keyc0tVaxhsnIA"
        text_question = request.form['text-question']
        adress_answer, lat_answer, lng_answer = creating_map_infos(text_question, MAP_KEY)
        url_answer, summary_answer = wiki_parsing(adress_answer)
        return render_template('index.html', summary=summary_answer, url=url_answer,
         adress_ans=adress_answer, lat_ans=lat_answer, lng_ans=lng_answer)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)