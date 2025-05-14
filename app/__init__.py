from flask import Flask
from random import randint
from flask import render_template

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("pages/home.jinja")

@app.get("/test/")
def test():
    return render_template("pages/test.jinja")

@app.get("/cool button/")
def coolButton():
    return render_template("pages/nuts.jinja")


@app.get("/random/")
def random():
    randNum = randint(1, 1000)
    return render_template("pages/random.jinja", number = randNum)

@app.errorhandler(404)
def notFound(error):
    return render_template("pages/404.jinja")