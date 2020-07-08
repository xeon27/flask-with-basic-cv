from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class QueryForm(FlaskForm):
    query = StringField('Query', validators=[DataRequired()])
    submit = SubmitField('Submit')


class ImageForm(FlaskForm):
    image = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images Only')])
    upload = SubmitField('Upload')


class ViewForm(FlaskForm):
    edgev = SubmitField('Vertical Edges')
    edgeh = SubmitField('Horizontal Edges')
    gray = SubmitField('Gray Scale')
    org = SubmitField('Original')