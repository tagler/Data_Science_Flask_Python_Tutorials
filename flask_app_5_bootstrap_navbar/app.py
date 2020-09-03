# debug mode: export FLASK_ENV=development
# run via: export FLASK_APP=app.py, flask run
# web server will run at http://127.0.0.1:5000/

from flask import Flask, render_template, request
app = Flask(__name__)

# navigation bar
from flask_nav import Nav
from flask_nav.elements import Navbar, View, Link
nav = Nav()
nav.register_element(
  'top',
  Navbar(
    View('Text Function App', 'index'),
    View('About', 'about'),
    View('Contact', 'contact'),
    Link('Google', 'https://www.google.com'),
  )
)
nav.init_app(app)

# bootstrap css
from flask_bootstrap import Bootstrap
Bootstrap(app)

@app.route('/', methods = ['POST', 'GET'])
def index():
    # post
    if request.method == 'POST':
      text = request.form['input']
      result = text.upper()
      return render_template("result.html", result=result)
    # get
    return render_template('index.html')

@app.route('/about')
def about():
  about = "About text..."
  return render_template('about.html', about=about)
    
@app.route('/contact')
def contact():
  contact = "Contact text..."
  return render_template('contact.html', contact=contact)
    