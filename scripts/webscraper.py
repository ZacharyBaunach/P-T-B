import json
import requests
#url = "https://play.pokemonshowdown.com/data/learnsets.json?utm_source=chatgpt.com"
loc = "db/Webscraped.JSON"
movesSetlocation = "db/Moveset.JSON"

testDic = {'learnset': 1}


with open(loc, 'r') as file:
    data = json.load(file)

moveSet = {}
with open(movesSetlocation, "w", encoding="utf-8") as f:
    for pokemon, moveDic in data.items():
        print(pokemon) #pokemon str name
        for learnset, moveList in moveDic.items():
            if (learnset == 'learnset'):
                if (moveList.keys() != type(testDic)):
                    moveSet[pokemon] = list(moveList.keys())
    
    json.dump(moveSet, f)
    print(f"Successfully downloaded and saved to {movesSetlocation}")

# if response.status_code == 200:
#     with open(loc, "w", encoding="utf-8") as f:
#         f.write(response.text)
#     print(f"Successfully downloaded and saved to {loc}")
# else:
#     print(f"Failed to fetch data. Status code: {response.status_code}")