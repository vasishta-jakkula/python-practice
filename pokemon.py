import random
# pokedex
pokedex = {
      "pikachu" : {"health": 30, "type": "electric", "damage": 10,"special_effect":"electric ball", "defense":0},
      "charizard" : {"health":20, "type": "fire", "damage": 20,"special_effect":"fire-spin","defense":0},
      "squirtle" : {"health": 25,"type":"water","damage": 11,"special_effect":"water-gush","defense":0},
      "eevee" : {"health": 30, "type":"special", "damage": 11, "special_effect":"peek-a-boo!","defense":0},
}
for key in pokedex.keys():
    print(f"{key}:{pokedex[key]}\n")
#add weaknesses and special moves later
user_pokemon_name = input("pick a pokemon to battle with(type exact name as shown in pokedex) \n")

#stats area
if user_pokemon_name in pokedex:
      pokemon_stats = pokedex[user_pokemon_name]
      print(f"stats of {user_pokemon_name} are {pokemon_stats}")
else:
        print("invalid registry of pokemon")

if user_pokemon_name in pokedex:
    input_continue = input("say yes if you would like to continue\n")
    if input_continue == "yes" or input_continue == "Yes":
        opponent_pokemon_name = ""
        while True:
            random_pokemon_index = random.randint(0, len(pokedex)-1)
            opponent_pokemon_name = list(pokedex.keys())[random_pokemon_index]
            if opponent_pokemon_name != user_pokemon_name:
                  break
        print(f"got your opponent is {opponent_pokemon_name}\n")
    elif input_continue == "no":
        print("you said no. So I stop")
        quit()
    else:
        print("invalid try again")

input_battle_1 = input(f"you chose {user_pokemon_name} as your pokemon in battle, what would you like to do?(type the number)\n 1. attack\n 2. Defense\n 3. Lucky shot(has a chance to do special effect)\n")
while True:
    #player battle
        
    #damage mechanic
    if input_battle_1 == "1":
        print(f"you attacked {opponent_pokemon_name}")

    #defense mechanics
    elif input_battle_1 == "2":
        user_pokemon_value = pokedex[user_pokemon_name]
        print(f"you defended your pokemon,{user_pokemon_value}.")
        user_pokemon_value["defense"] = user_pokemon_value["defense"] + 1
        print(f"your defense level is {user_pokemon_value['defense']}")
        print(f"{opponent_pokemon_name}will now go.")

    #special move mechanics
    elif input_battle_1 == "3":
        print("#SPECIAL MOVE CODE NEEDED")
    # when battle is won or lost, print message
    #explore for a account type of approach 
    else:
         print("invalid response")
