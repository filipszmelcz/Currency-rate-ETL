import requests
import csv

base_url = "https://pokeapi.co/api/v2/"

def load_pokemon_info():
            url = f"{base_url}/pokemon?limit=10"
            response = requests.get(url)

            if response.status_code == 200:
                info = response.json()
                print("Data transfer complete")
                return info
            else:
                print(f"Wrong data")

pokemon_data = load_pokemon_info()
if pokemon_data:
    print(pokemon_data["results"])
    pokemon_data_results = pokemon_data["results"]
    with open("load_pokemon_info.csv", "w", newline="") as f:
        w = csv.DictWriter(f, pokemon_data_results[0].keys())
        w.writeheader()
        w.writerows(pokemon_data_results)