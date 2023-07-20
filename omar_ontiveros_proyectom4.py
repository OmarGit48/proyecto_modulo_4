
# empezamos con la libreria requests
import requests
import json
import os
import matplotlib.pyplot as plt 
from PIL import Image
from urllib.request import urlopen

pokemon = input('pon un pokemon: ')

url = "https://pokeapi.co/api/v2/pokemon/" +pokemon
respuesta = requests.get(url)

if respuesta.status_code != 200 :
    print ("Algo salio mal, el pokemon no existe")
    exit()
    
datos = respuesta.json()

name = datos["name"]
print("This is the pokemon: ", name)

print("\nHis moves are: ")
moves = datos["moves"]
for i in range(int(len(moves))):
    move = moves[i]["move"]["name"]
    print(move)

weight = datos["weight"]
print("\nhis weight is: ", weight)

height = datos["height"]
print("\nhis height is:  ", height)

print("\nThe abilities are: ")
abilities = datos["abilities"]
for u in range(int(len(abilities))):
    ability = abilities[u]["ability"]["name"]
    print(ability)

types = datos["types"]
for e in range(int(len(types))):
    type = types[e]["type"]["name"]
    print(type)
try:
    url_imagen = datos["sprites"]["front_default"]    
    imagen = Image.open(urlopen(url_imagen))
    plt.title(datos["name"])
    imgplot = plt.imshow(imagen)
    plt.show()
except:
    print("El pokemon no tiene imagen")
    exit()
 
if not os.path.exists("pokedex"):
    os.makedirs("pokedex")    

pokemon_data = {
    "name": name,
    "moves": [move for move in moves],
    "weight": weight,
    "height": height,
    "abilities": [ability for ability in abilities],
    "types": [type for type in types],
    "image_url": url_imagen
}
with open("pokedex.json", "w") as json_file:
    json.dump(pokemon_data, json_file, indent=4)

print(f"Datos del Pokémon guardados en el archivo 'pokedex/pokemon_data.json'")
