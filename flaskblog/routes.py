from flask import render_template, url_for, flash, redirect
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        "author": "Georgina Bartlett",
        "title": "Learning Flask",
        "content": "Learning to create a website using Python!",
        "date_posted": "July 23rd"
    },
    {
        "author": "Hector Bartlett",
        "title": "Eating and Sleeping",
        "content": "I love peanut butter and I keep waking my mum up by having really loud dreams",
        "date_posted": "July 24th"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods = ["GET", "POST"])  # tell method to accept get and post
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()  # create an instance of the form
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')  # .decode returns a string instead of bytes
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)  #need to return the hashed password not the plain text
        db.session.add(user)
        db.session.commit()
        flash(f"Welcome {form.username.data}! Your account has been created. You can now log in!", "success")
        return redirect(url_for("login"))  # naming function not route
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()  # create an instance of the form
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)  # check True/uncheck False
            return redirect(url_for("home"))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

# create a logout function to return user to home when they logout
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

# create a route to user's account
@app.route("/account")
def account():
    return render_template('account.html', title='Account')
