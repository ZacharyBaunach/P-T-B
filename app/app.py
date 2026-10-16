from flask import Flask, render_template

app = Flask(__name__)


@app.route("/template")
def home():
    name = "Zachary"
    return render_template("template.html")

@app.route("/hello")
def hello():
    return "Hello, World! My favorite Eeveelution is Glaceon."

@app.route("/TheForbiddenPage")
def TheForbiddenPage():
    return "You have stumbled upon sights unmeant for your eyes. Turn back or be forever lost."

