import requests
url = "https://play.pokemonshowdown.com/data/learnsets.json?utm_source=chatgpt.com"
loc = "app/db"

response = requests.get(url)

if response.status_code == 200:
    with open(loc, "w", encoding="utf-8") as f:
        f.write(response.text)
    print(f"Successfully downloaded and saved to {loc}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")