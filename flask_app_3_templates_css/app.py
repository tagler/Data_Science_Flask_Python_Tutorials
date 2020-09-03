# debug mode: export FLASK_ENV=development
# run via: export FLASK_APP=app.py, flask run
# web server will run at http://127.0.0.1:5000/
# html files in ./templates/
# css files in ./static/styles/

from flask import Flask, render_template
app = Flask(__name__)

sample_message = "Hello World!"
sample_list = ["Thing 1", "Thing 2", "Thing 3"]

@app.route('/')
def index():
    return render_template(
        # html file
        "index.html", 
        # variables 
        my_message=sample_message,
        my_list=sample_list
    )