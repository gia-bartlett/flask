from datetime import datetime
from flaskblog import db

# models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # creating a column and specifying the datatype
    username = db.Column(db.String(20), unique=True, nullable=False)  # set length, and not null
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)  # set length (hash), and not null
    posts = db.relationship('Post', backref='author', lazy=True)  # post attribute has a relationship to Post Model (class)

    def __repr__(self):  # how our object is printed whenever we print it out
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
