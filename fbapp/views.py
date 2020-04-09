from flask import Flask, render_template

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
#app.config.from_object('config')

@app.route('/')
def index():
    hey = '"Bien sûr mon poussin ! La voici : 7 cité Paradis, 75010 Paris"'
    return render_template('index.html', exact=hey)

if __name__ == "__main__":
    app.run()