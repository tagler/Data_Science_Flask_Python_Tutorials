# debug mode: export FLASK_ENV=development
# run via: export FLASK_APP=app.py, flask run
# web server will run at http://127.0.0.1:5000/

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Index Page"

@app.route('/about/')
def about():
    return "About Page"

@app.route('/<name>')
def hello_name(name):
    return f"Hello {name}!"