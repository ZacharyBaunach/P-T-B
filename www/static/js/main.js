console.log("main.js loaded - edit me in www/static/js/main.js");

//grab containers from page
const Search = document.getElementById("pokeEntry")
const resultsList = document.getElementById("resultsList")
//init search list results
let data = []

//fetch Pokedex.JSON
fetch('Pokedex.JSON')
    .then(jsonData => {
        data = jsonData; 
    })


Search.addEventListener('input', (e) => {
    const searchString = e.target.value.toLowerCase();

    // Filter data based on user input
    const filteredData = data.filter(item => {
        return item.name.toLowerCase().includes(searchString);
    });

    displayResults(filteredData);
});

// 3. Display the filtered results in the HTML
function displayResults(items) {
    // Clear previous results
    resultsList.innerHTML = '';

    // If no matches found
    if (items.length === 0) {
        resultsList.innerHTML = '<li>No results found</li>';
        return;
    }
}