import requests
import csv

base_url = "https://pokeapi.co/api/v2/"

def load_pokemon_to_csv():
    url = f"{base_url}/pokemon?limit=10000"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        print("Data transfer complete")
    else:
        print(f"Wrong data")
    
    if pokemon_data:
        pokemon_data_results = pokemon_data["results"]
        with open("load_pokemon_info.csv", "w", newline="") as f:
            w = csv.DictWriter(f, pokemon_data_results[0].keys())
            w.writeheader()
            w.writerows(pokemon_data_results)

load_pokemon_to_csv()