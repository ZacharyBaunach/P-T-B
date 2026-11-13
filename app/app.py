from flask import Flask, render_template
import json

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

@app.route("/Pokedex")
def getPokeData():
    with open('db/Pokedex.json', 'r', encoding='utf-8') as file:
        pokedex = json.load(file)
        return pokedex

@app.route("/PokeMoves")
def getPokeMoves():
    with open('db/Moveset.json', 'r', encoding='utf-8') as file:
            pokeMoves = json.load(file)
            return pokeMoves

@app.route("/Pokemon/<id>")
def pokemonProfile(id):
    with open('db/Pokedex.json', 'r', encoding='utf-8') as file:
        pokedex = json.load(file)

    FIRSTPOKEMON = 0
    LASTPOKEMON = 646
    
    pd = pokedex[int(id)-1]

    with open('db/Moveset.json', 'r', encoding='utf-8') as file:
        pokeMoves = json.load(file)

    ms = pokeMoves[str(pd['name'].lower())]
    
    if int(id) <= FIRSTPOKEMON:
        prevPkm = pokedex[LASTPOKEMON]
        prevID = LASTPOKEMON 
    else:
        prevPkm = pokedex[int(id)-2]

        prevID = int(id)-1

    
    if int(id) > LASTPOKEMON:
        nextPkm = pokedex[FIRSTPOKEMON]
        nextID = 1
    else:
        nextPkm = pokedex[int(id)]
        nextID = int(id)+1
    
    
    return render_template('pokemon.html', pokedex=pd, pokeMoves=ms, prevPkm=prevPkm, nextPkm=nextPkm, prevID=prevID, nextID=nextID)