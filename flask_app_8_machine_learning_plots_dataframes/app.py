# debug mode: export FLASK_ENV=development
# run via: export FLASK_APP=app.py, flask run
# web server will run at http://127.0.0.1:5000/

import pickle
import numpy as np 
import pandas as pd 

from flask import Flask, render_template, request, flash
app = Flask(__name__)

# note: wtforms requires secret key
# for production use: app.config.from_pyfile('config.py')
# make sure you do not commit secret key to public repo
app.config['SECRET_KEY'] = 'enter_secret_key_here'

# navigation bar
from flask_nav import Nav
from flask_nav.elements import Navbar, View, Link, Subgroup, Separator
nav = Nav()
nav.register_element(
  'top',
  Navbar(
    View('Iris Machine Learning App', 'index'),
    View('Plots', 'plots'),
    View('Dataframe', 'dataframe'),
    View('About', 'about'),
    View('Contact', 'contact'),
    Subgroup(
        'External Links',
        Link('University of Notre Dame', 'https://www.nd.edu'),
        Link('Northwestern University', 'https://www.northwestern.edu'),
        Separator(),
        Link('Google', 'https://www.google.com'),
    ),
  )
)
nav.init_app(app)

# bootstrap css
from flask_bootstrap import Bootstrap
Bootstrap(app)

# wtforms
from forms import MyForm 

# sklearn machine learning model
with open("./model/model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/', methods = ['POST', 'GET'])
def index():
    form = MyForm()
    # post
    if form.validate_on_submit():
      # extract form input data
      sepal_length = form.sepal_length.data
      sepal_width = form.sepal_width.data
      petal_length = form.petal_length.data
      petal_width = form.petal_width.data
      # model prediction
      feature_list = [sepal_length, sepal_width, petal_length, petal_width]
      feature_array = np.array(feature_list).reshape(1, -1)
      result_string = model.predict(feature_array)[0]
      prediction = result_string[0].upper() + result_string[1:]
      return render_template('predict.html', prediction=prediction)
    # get
    return render_template('index.html', form=form)

# plotly visualizations
import visuals

@app.route('/plots')
def plots():
  # load data
  df = pd.read_csv("./data/data.csv")
  # create plots 
  plot_1 = visuals.create_histogram(df)
  plot_2 = visuals.create_scatterplot(df)
  plot_3 = visuals.create_barplot(df)
  return render_template(
    'plots.html', 
    plot_1=plot_1, 
    plot_2=plot_2,
    plot_3=plot_3,
  )

# dataframe display 
@app.route('/dataframe')
def dataframe():
  # load data
  df = pd.read_csv("./data/data.csv")
  return render_template(
    'dataframe.html', 
    dataframe=df.to_html(
      classes=[
        "table",
        "table-striped",
        "table-hover",
        "table-condensed",
      ]
    )
  )

# simple page with if else statement and for loop
@app.route('/about')
def about():
  about = "This application uses the Iris dataset to predict the species of a flower."
  my_boolean = True
  my_list = ["setosa","versicolor","virginica"]
  return render_template(
    'about.html', 
    about=about,
    my_boolean = my_boolean,
    my_list = my_list,
  )
  
# simple page with text
@app.route('/contact')
def contact():
  contact = 'Contact via <a href="mailto:support@email.com">Email</a>'
  return render_template('contact.html', contact=contact)
    