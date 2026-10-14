from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/template")
def home():
    return render_template("template.html")

@app.route("/Pokedex")
def getPokeData():
    with open('db/Pokedex.json', 'r', encoding='utf-8') as file:
        pokedex = json.load(file)
        return pokedex
