from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField,SelectField
from wtforms.validators import DataRequired, Email, Length
from app.Auth.model import TypeUsers

class SignupForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=64)])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
   # type = SelectField('TypeUser',validators=[DataRequired] )
    submit = SubmitField('Registrar')
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Recuérdame')
    submit = SubmitField('Login')