from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        "author": "Georgina Bartlett",
        "title": "Learning Flask",
        "content": "Learning to create a website using Python!",
        "date": "July 23rd"
    },
    {
        "author": "Hector Bartlett",
        "title": "Eating and Sleeping",
        "content": "I love peanut butter and I keep waking my mum up by having really loud dreams",
        "date": "July 24th"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)