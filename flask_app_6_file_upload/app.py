# debug mode: export FLASK_ENV=development
# run via: export FLASK_APP=app.py, flask run
# web server will run at http://127.0.0.1:5000/

import pandas as pd 

from flask import Flask, render_template, request
app = Flask(__name__)

# navigation bar
from flask_nav import Nav
from flask_nav.elements import Navbar, View, Link
nav = Nav()
nav.register_element(
  'top',
  Navbar(
    View('File Upload App', 'index'),
    View('About', 'about'),
    View('Contact', 'contact'),
    Link('Google', 'https://www.google.com'),
  )
)
nav.init_app(app)

# bootstrap css
from flask_bootstrap import Bootstrap
Bootstrap(app)

# upload files
upload_dir = './upload/'

@app.route('/', methods = ['POST', 'GET'])
def index():
    # post
    if request.method == 'POST':
      # upload file
      uploaded_file = request.files['csv_file']
      # save file
      uploaded_file.save(upload_dir + uploaded_file.filename)
      # read file
      data = pd.read_csv(upload_dir + uploaded_file.filename, header=None)
      data.columns = ['numbers']
      # process file
      result_count = data['numbers'].count()
      result_sum = data['numbers'].sum()
      result_max = data['numbers'].max()
      result_min = data['numbers'].min()
      return render_template("result.html", 
        result_count=result_count,
        result_sum=result_sum,
        result_max=result_max,
        result_min=result_min,
        )
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
    