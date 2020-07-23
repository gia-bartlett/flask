from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = '35b4aba7a69ce7830f6a23c80257a987'

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

@app.route("/register")
def register():
    form = RegistrationForm()  # create an instance of the form
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()  # create an instance of the form
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)