from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("pages/home.jinja")

@app.get("/test/")
def test():
    return render_template("pages/test.jinja")
@app.get("/umIDK/")
def umIDK():
    return "<h1>Testing... My brain cells</h1>"