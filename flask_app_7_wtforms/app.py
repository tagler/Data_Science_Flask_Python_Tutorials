# debug mode: export FLASK_ENV=development
# run via: export FLASK_APP=app.py, flask run
# web server will run at http://127.0.0.1:5000/

from flask import Flask, render_template, request, flash
app = Flask(__name__)

# note: wtforms requires secret key
# for production use: app.config.from_pyfile('config.py')
# make sure you do not commit secret key to public repo
app.config['SECRET_KEY'] = 'enter_secret_key_here'

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

# wtforms
from forms import MyForm 

@app.route('/', methods = ['POST', 'GET'])
def index():
    form = MyForm()
    # post
    if form.validate_on_submit():
      # extract form input data
      input_value = form.name.data
      result = input_value.upper()
      return render_template('result.html', result=result)
    # get
    return render_template('index.html', form=form)

@app.route('/about')
def about():
  about = "About text..."
  return render_template('about.html', about=about)
    
@app.route('/contact')
def contact():
  contact = "Contact text..."
  return render_template('contact.html', contact=contact)
    