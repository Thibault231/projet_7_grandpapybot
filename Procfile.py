# coding: utf-8
web: gunicorn fbapp:app
init: FLASK_APP=run.py