import random

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

def computer_wins(self):
    print(f"{self} WINS!!")
    print("Computer Wins")
    return player_wins

def player_wins(self):
    print(f"{self} WINS!!")
    print("You Win")



def determine_winner(matchesA, matchesB, random_winner, player_win_count, computer_win_count):
    for x,y in zip(matchesA, matchesB):
        if x['level'] < y['level']:
            computer_wins(y['name'])
            computer_win_count += 1
        elif x['level'] > y['level']:
            player_wins(x['name'])
            player_win_count += 1
        elif x['level'] == y['level']:
            if x['type'] == "Fire" and y['type'] == 'Grass':
                player_wins(x['name'])
            elif x['type'] == "Grass" and y['type'] == 'Water':
                player_wins(x['name'])             
            elif x['type'] == "Water" and y['type'] == 'Fire':
                player_wins(x['name'])
            elif x['type'] == "Electric" and y['type'] == 'Water':
                player_wins(x['name'])
                ###                                        
            elif x['type'] == "Water" and y['type'] == 'Grass':
                computer_wins(y['name'])
            elif x['type'] == "Fire" and y['type'] == 'Water':
                computer_wins(y['name'])
            elif x['type'] == "Grass" and y['type'] == 'Fire':
                computer_wins(y['name'])
            elif x['type'] == "Water" and y['type'] == 'Electric':
                computer_wins(y['name'])               
            else:
                if random_winner == x['name']:
                    print(random_winner,"is the Winner")
                    print("You Win")    
                else:
                    print(y['name'],"is the Winner")
                    print("Computer Win")
        elif x['name'] == y['name']:
            print(random_winner,"is the Winner")
            print(random.choice(["You","Computer"]),"Wins")
        else:
            if random_winner == x['name']:
                print(random_winner,"is the Winner")
                print("You Win")    
            else:
                print(y['name'],"is the Winner")           
                print("Computer Win")
    return