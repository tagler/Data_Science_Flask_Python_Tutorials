# debug mode: export FLASK_ENV=development
# run via: export FLASK_APP=app.py, flask run
# web server will run at http://127.0.0.1:5000/

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    # post
    if request.method == 'POST':
      text = request.form['input']
      result = text.upper()
      return render_template("result.html", result=result)
    # get
    return render_template('index.html')


    