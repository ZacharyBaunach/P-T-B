console.log("main.js loaded - edit me in www/static/js/main.js");

//inits
// TEAM_LIMIT = max team members, MOVE_LIMIT = max moves
const TEAM_LIMIT = 6
const MOVE_LIMIT = 4
// list of pokemon to add (for adding session storage)
let pokeSearchList = []
// Holds the Pokedex data and Pokemon Move data fetched from the server
let pokeData = [];
let pokeMoves = [];

// Event listener waiting for DOM content load to fetch Pokedex database entries
document.addEventListener('DOMContentLoaded', function() {
    console.log("Loaded page");
    pageLoad();
});

// ---- RESTORE SAVED TEAM ----
//checks sessionStorage and loads in 'saved' team
// Restores previously saved team selections from browser session storage on load
// Check each of the 6 slots for saved data and re-add it
async function loadTeam() {
    for (let p = 1; p <= TEAM_LIMIT; p++) {
        if (sessionStorage[p]){
            pokeSearchList.push(JSON.parse(sessionStorage.getItem(p)))
            console.log(`loading index ${p}`)
            pokeAdd(undefined,p-1)
            pokeSearchList.pop()
        }   else {
            console.log(`empty session storage of index ${p}`)
        }
    }
}

// creates img DOM element given pokemon name
function image(name){
    const pokeImage = document.createElement('img')
    pokeImage.setAttribute('src', `static/img/pokemon_collection/${name}.webp`)
    pokeImage.setAttribute('alt', `${name} sprite`)
    pokeImage.setAttribute('class', 'pokeSprite')
    return pokeImage
}

// Stat Calc for hp
function hpStatCalc(baseVal, IV = 0, EV = 0, level = 50) {
    const actualVal = ((2*baseVal + IV + EV/4)*level)/100+level+10
    return actualVal
}
// Sstat Calc for atk, def, spa, spd, spe
function statCalc(baseVal, IV = 0, EV = 0, level = 50, nature = 1) {
    const actualVal = (((2*baseVal + IV + EV/4)*level)/100+5) * nature
    return actualVal
}