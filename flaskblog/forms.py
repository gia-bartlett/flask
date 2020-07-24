from flask_wtf import FlaskForm  # Extension for working with forms in Flask
from wtforms import StringField, PasswordField, SubmitField, BooleanField  # classes
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError  # prevents an empty string and limits character length
from flaskblog.models import User

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

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):  # inherits from FlaskForm
    # login using email
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')  # stay logged in using cookies
    submit = SubmitField('Login')
