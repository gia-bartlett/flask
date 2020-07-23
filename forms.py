from flask_wtf import FlaskForm  # Extension for working with forms in Flask
from wtforms import StringField, PasswordField, SubmitField, BooleanField  # classes
from wtforms.validators import DataRequired, Length, Email, EqualTo  # prevents an empty string and limits character length

# Making a new file to keep things separate and manageable

# Allows us to write forms in Python that are converted into HTML
class RegistrationForm(FlaskForm):  # inherits from FlaskForm
    # form fields
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    # validators are added as arguments to make sure we get what we want from the user
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):  # inherits from FlaskForm
    # login using email
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')  # stay logged in using cookies
    submit = SubmitField('Login')
