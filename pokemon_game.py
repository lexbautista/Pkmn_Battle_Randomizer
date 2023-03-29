import random
import json
import subprocess


subprocess.run(["clear"])
print('Battle your computer with Pokemon \n'
    + "if your bored just try it \n")

# Load the JSON file
with open('pokemon_data.json', 'r') as f:
    data = json.load(f)

# Print the name,type, level of each pokemon
player1_pokemon = random.choice(data['pokemon'])
player2_pokemon = random.choice(data['pokemon'])
print("You randomly choose",player1_pokemon['name'], "versus your Computer who randomly pick", player2_pokemon['name'])
print(player1_pokemon['name'], "VS", player2_pokemon['name'])

#Let the Battle Begin.
def search_json(key, value, data):
    matches = []
    if isinstance(data, dict):
        for k, v in data.items():
            if k == key and v == value:
                matches.append(data)
            elif isinstance(v, (dict, list)):
                matches += search_json(key, value, v)
    elif isinstance(data, list):
        for item in data:
            matches += search_json(key, value, item)
    return matches

# Search for data by key and value
key = 'name'
value1 = player1_pokemon['name']
matchesA = search_json(key, value1, data)
value2 = player2_pokemon['name']
matchesB = search_json(key, value2, data)

#Let the battle Begins 
# I need to create a function for this

for x,y in zip(matchesA, matchesB):
    if x['level'] < y['level']:
        print(y['name'], "WINS!!")
    elif x['level'] > y['level']:
        print(x['name'], "WINS!!")
    elif x['level'] == y['level']:
        if x['type'] == "Fire" and y['type'] == 'Grass':
            print(x['name'], "WINS!!")
        elif x['type'] == "Grass" and y['type'] == 'Water':
            print(x['name'], "WINS!!")
        elif x['type'] == "Water" and y['type'] == 'Fire':
            print(x['name'], "WINS!!")
        elif x['type'] == "Water" and y['type'] == 'Grass':
            print(y['name'], "WINS!!")
        elif x['type'] == "Fire" and y['type'] == 'Water':
            print(y['name'], "WINS!!")
        elif x['type'] == "Grass" and y['type'] == 'Fire':
            print(y['name'], "WINS!!")
        else:
           print("Its a TIE!!") 
    else:
        print("Its a TIE!!")




    
