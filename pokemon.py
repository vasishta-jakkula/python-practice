import random
# pokedex
pokedex = {
      "pikachu" : {"health": 30, "type": "electric", "damage": 10,"special_effect":"electric ball"},
      "charizard" : {"health":20, "type": "fire", "damage": 20,"special_effect":"fire-spin"},
      "squirtle" : {"health": 25,"type":"water","damage": 11,"special_effect":"water-gush"},
      "eevee" : {"health": 30, "type":"special", "damage": 11, "special_effect":"peek-a-boo!"},
}
for key in pokedex.keys():
    print(f"{key}:{pokedex[key]}\n")
#add weaknesses and special moves later
user_pokemon = input("pick a pokemon to battle with(type exact name as shown in pokedex) \n")

#stats area
if user_pokemon in pokedex:
      pokemon_stats = pokedex[user_pokemon]
      print(f"stats of {user_pokemon} are {pokemon_stats}")
else:
        print("invalid registry of pokemon")

if user_pokemon in pokedex:
    input_continue = input("say yes if you would like to continue\n")
    if input_continue == "yes" or input_continue == "Yes":
        random_pokemon = ""
        while True:
            random_pokemon_index = random.randint(0, len(pokedex)-1)
            random_pokemon = list(pokedex.keys())[random_pokemon_index]
            if random_pokemon != user_pokemon:
                  break
        print(f"got your opponent is {random_pokemon}\n")
    elif input_continue == "no":
        print("you said no. So I stop")
    else:
        print("invalid try again")

input_battle_1 = input(f"you chose {user_pokemon} as your pokemon in battle, what would you like to do?(type the number)\n 1. attack\n 2. Defense\n 3. Lucky shot(has a chance to do special effect)\n")

if input_battle_1 == "1":
    print(f"you attacked {random_pokemon}")
if input_battle_1 == "2":
    print(f"you defended your pokemon,{user_pokemon}.")
if input_battle_1 == "3":
    print("#SPECIAL MOVE CODE NEEDED")