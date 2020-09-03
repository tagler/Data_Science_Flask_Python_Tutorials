from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    sepal_length = FloatField('Sepal Length:', validators=[DataRequired()])
    sepal_width = FloatField('Sepal Width:', validators=[DataRequired()])
    petal_length = FloatField('Petal Length:', validators=[DataRequired()])
    petal_width = FloatField('Petal Width:', validators=[DataRequired()])
    submit = SubmitField('Submit')