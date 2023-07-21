
# Start with the library
import requests
import json
import os
import matplotlib.pyplot as plt 
from PIL import Image
from urllib.request import urlopen

pokemon = input("\nGive me a pokemon name: ") # asking for a pokemon name

url = "https://pokeapi.co/api/v2/pokemon/" +pokemon
answer = requests.get(url)
"""Put the url where we get information to consult"""

if answer.status_code != 200 : # i use the status_code and print answer
    print ("Something is wrong, the pokemon is not exist")
    exit()
    
data = answer.json() # creat json's file

name = data["name"]  # get the name of the pokemon and print
print("\nThis is the pokemon: ", name)

print("\nHis moves are: ") #get and print the pokemon's moves
moves = data["moves"]
for i in range(int(len(moves))):
    move = moves[i]["move"]["name"]
    print(move)

weight = data["weight"] # get the pokemon's weight and print
print("\nhis weight is: ", weight)

height = data["height"] # get the pokemon's height and print
print("\nhis height is:  ", height)

print("\nThe abilities are: ")
abilities = data["abilities"] # get the pokemon's abilities and print
for u in range(int(len(abilities))):
    ability = abilities[u]["ability"]["name"]
    print(ability)

types = data["types"] # get the pokemon's types and print
for e in range(int(len(types))):
    type = types[e]["type"]["name"]
    print(type)
    
try:
    url_imagen = data["sprites"]["front_default"] # try to get the pokemon's image if have it
    image = Image.open(urlopen(url_imagen))
    plt.title(data["name"])
    imgplot = plt.imshow(image)
    plt.show()
except:
    print("We don't have image of the pokemon") # give answer when ww haven't image
    exit()
 
if not os.path.exists("pokedex"): # make a fiel pokedex if we don't have it
    os.makedirs("pokedex")    

#get pokemon's information for save in the file pokedex
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

print(f"Pokemon data is saved 'pokedex/pokemon_data.json'")
