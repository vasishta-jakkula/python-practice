import random
# pokedex
shop_pokemon = ""
money = 10
pokedex = {
      "pikachu" : {"health": 30, "type": "electric", "damage": 10,"defense":0},
      "charizard" : {"health": 30, "type": "fire", "damage": 9,"defense":0},
      "squirtle" : {"health": 25,"type":"water","damage": 11,"defense":0},
      "eevee" : {"health": 30, "type":"special", "damage": 11,"defense":0},
}
inventory = {
      "health_charm" : 1,
      "strength_charm" : 0
}
for key in pokedex.keys():
    print(f"{key}:{pokedex[key]}\n")
#add weaknesses and special moves later
start_input = input("(type num) what would you like to do 1. fight 2. buy pokemon\n")

#shop
if start_input == "2":
       print(f"hello welcome to the shop, you may buy pokemon here\n")
       shop_pokemon == {
              "bulbasaur" : {"health": 30, "type": "grass","damage": 12,"defense":0,"price": 25},
              "scorbunny" : {"health": 30, "type":"fire","damage": 12,"defense":0, "price" : 35},
              "lobunny"  : {"health": 40,"type":"earth","damage":15,"defense":0,"price": 40},
              "taillow" : {"health": 27,"type":"flying","damage":8,"defense":0,"price": 15},
              "litten" : {"health": 35,"type":"fire","damage" : 13,"defense":0,"price": 20},
              }
       for shop_keys in shop_pokemon.keys():
            print(f"{shop_keys}:{shop_pokemon[key]}\n")



#battle
if start_input == "1":
      user_pokemon_name = input("pick a pokemon to battle with(type exact name as shown in pokedex) \n")\
      #stats area
      if user_pokemon_name in pokedex:
            pokemon_stats = pokedex[user_pokemon_name]
            print(f"stats of {user_pokemon_name} are {pokemon_stats}")
      else:
            print("invalid registry of pokemon")
      opponent_attack = ""
      user_pokemon_value = pokedex[user_pokemon_name]
      opponent_pokemon_name = ""
      opponent_pokemon_value = {}
      if user_pokemon_name in pokedex:
       input_continue = input("say yes if you would like to continue\n")
      if input_continue == "yes" or input_continue == "Yes":
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

      input_battle_1 = input(f"you chose {user_pokemon_name} as your pokemon in battle, what would you like to do?(type the number)\n 1. attack\n 2. Defense\n 3. check items for a bonus \n")
            #player battle
                  
            #damage mechanic

      if input_battle_1 == "1":

                  print(f"you attacked {opponent_pokemon_name}")
                  opponent_pokemon_value = pokedex[opponent_pokemon_name]
                  opponent_pokemon_value["health"] = opponent_pokemon_value["health"] - user_pokemon_value["damage"]
                  if opponent_pokemon_value["health"] == 0:
                        print("you won, congrats")
                        quit()
                  print(f"your opponent,{opponent_pokemon_name}, has {opponent_pokemon_value['health']} left \n")
                  print(f"{opponent_pokemon_name} will now go.\n")
                  opponent_attack = random.randint(1,3)
                  if opponent_attack == 1:
                        opponent_pokemon_value["defense"] = opponent_pokemon_value["defense"] + 1
                        print(f"your opponent has {opponent_pokemon_value['defense']} defense level now")
                  if opponent_attack == 2:
                        user_pokemon_value['health'] = opponent_pokemon_value["damage"] - user_pokemon_value["health"]
                        print(f"your {opponent_pokemon_name} has attacked you you have now {user_pokemon_value['health']}")
                  
            
            #defense mechanics
      elif input_battle_1 == "2":
                  print(f"you defended your pokemon,{user_pokemon_value}.")
                  user_pokemon_value["defense"] = user_pokemon_value["defense"] + 1
                  print(f"your defense level is {user_pokemon_value['defense']}\n")
                  print(f"{opponent_pokemon_name} will now go.\n")
                  opponent_attack = random.randint(1,3)
                  if opponent_attack == 1:
                        opponent_pokemon_value["defense"] = opponent_pokemon_value["defense"] + 1
                        print(f"your opponent has {opponent_pokemon_value['defense']} defense level now")
                  if opponent_attack == 2:
                        user_pokemon_value['health'] = user_pokemon_value["health"]-opponent_pokemon_value["damage"]
                        print(f"your {opponent_pokemon_name} has attacked you you have now {user_pokemon_value['health']}")
                        
                        

      # inventory mechanics
      elif input_battle_1 == "3":
            print(f"your inventory is composed of the following,\n{inventory}\n")
            print("# section in the works try again")
      else:
                  print("invalid response")
