import pandas as pd
import requests

def get_url(url):
    response = requests.get(url)
    return response.json()

def get_pokemon(data):
    pokemons_data = []
    pokemon_list = data["pokemon"]
    for pokemon in pokemon_list:
        nombre = pokemon["pokemon"]["name"]
        url = pokemon["pokemon"]["url"]
        pokemons_data.append({"Name": nombre, "URL": url})
    return pokemons_data


def converti_to_excel(pokemons_data, ruta_archivo):
    df = pd.DataFrame(pokemons_data)
    df.to_excel(ruta_archivo,index= False)
    print(f"Archivo guardado exitosamente como {ruta_archivo}")

def run():
    url = "https://pokeapi.co/api/v2/type/3"
    dato = get_url(url)
    get_pokemons = get_pokemon(dato)

    ruta_archivo = "Excelpokemons.xlsx"
    converti_to_excel(get_pokemons, ruta_archivo)
    return print(f"Se convierte el archivo {ruta_archivo}")


run()