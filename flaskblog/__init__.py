# imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


# configuration
app = Flask(__name__)
app.config["SECRET_KEY"] = '35b4aba7a69ce7830f6a23c80257a987'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # /// relative path from current file
db = SQLAlchemy(app)  # creating an instance of our database
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from flaskblog import routes  # import after app initialisation to prevent circular error
