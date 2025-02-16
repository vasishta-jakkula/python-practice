import random
pokedex = {
      "pikachu" : {"health": 30, "type": "electric", "damage": 10},
      "charizard" : {"health":20, "type": "fire", "damage": 20},
      "squirtle" : {"health": 25,"type":"water","damage": 11},
      "eevee" : {"health": 30, "type":"special", "damage": 11},
}
for key in pokedex.keys():
    print(f"{key}:{pokedex[key]}\n")
#add weaknesses and special moves later
input_of_pokemon = input("pick a pokemon to battle with(type exact name as shown in pokedex) \n")

#stats area
if input_of_pokemon in pokedex:
      pokemon_stats = pokedex[input_of_pokemon]
      print(f"stats of {input_of_pokemon} are {pokemon_stats}")
else:
        print("invalid registry of pokemon")

if input_of_pokemon in pokedex:
    input_continue = input("say yes if you would like to continue\n")
    if input_continue == "yes" or input_continue == "Yes":
        random_pokemon = ""
        while True:
            random_pokemon_index = random.randint(0, len(pokedex)-1)
            random_pokemon = list(pokedex.keys())[random_pokemon_index]
            if random_pokemon != input_of_pokemon:
                  break
        print(f"got your opponent is {random_pokemon}\n")
    elif input_continue == "no":
        print("you said no. So I stop")
    else:
        print("invalid try again")

