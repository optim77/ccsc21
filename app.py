from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def base():
    return render_template("base.html")


@app.route("/about")
def about():
    return "hi"