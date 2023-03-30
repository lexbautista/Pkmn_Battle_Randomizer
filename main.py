import random
import json
import subprocess
import pokemon_module


subprocess.run(["clear"])
print('Battle your computer with Pokemon \n'
    + "if your bored just try it \n"
    + "Priority is Level then Type \n")

# Load the JSON file
with open('pokemon_data.json', 'r') as f:
    data = json.load(f)

#Let the battle Begins 
for i in range(6):
    # Print the name of each pokemon
    player1_pokemon = random.choice(data['pokemon'])
    player2_pokemon = random.choice(data['pokemon'])
    print("You randomly choose",player1_pokemon['name'], "versus your Computer who randomly pick", player2_pokemon['name'])
    print(player1_pokemon['name'], "VS", player2_pokemon['name'])
    # Search for data by key and value
    key = 'name'
    value1 = player1_pokemon['name']
    matchesA = pokemon_module.search_json(key, value1, data)
    value2 = player2_pokemon['name']
    matchesB = pokemon_module.search_json(key, value2, data)
    random_winner = random.choice([value1, value2])
    player_win_count = 0
    computer_win_count = 0
    pokemon_module.determine_winner(matchesA, matchesB, random_winner, player_win_count, computer_win_count)    






    
