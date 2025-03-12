import random
# pokedex
shop_pokemon = ""
money = 10
inventory = {
      "health_charm" : 1,
      "strength_charm" : 0
}
pokedex = {
      "pikachu" : {"health": 30, "type": "electric", "damage": 10,"defense":0},
      "charizard" : {"health": 30, "type": "fire", "damage": 9,"defense":0},
      "squirtle" : {"health": 25,"type":"water","damage": 11,"defense":0},
      "eevee" : {"health": 30, "type":"special", "damage": 11,"defense":0},
}

while True:
      start_input = input("(type num) what would you like to do 1. fight 2. buy pokemon\n")

      #battle
      print("here are your pokemon\n")
      for key in pokedex.keys():
       print(f"{key}:{pokedex[key]}\n")

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
                  print("\n")
                  print(f"your opponent is {opponent_pokemon_name}\n")
            elif input_continue == "no":
                  print("you said no. So I stop")
                  quit()
            else:
                  print("invalid try again")




                  
            while True:
                        #player battle
                  input_battle_1 = input(f"{user_pokemon_name} is your pokemon in battle, what would you like to do?(type the number)\n 1. attack\n 2. Defense\n")
                  
                        #damage mechanic
                  if input_battle_1 == "1":

                              print(f"you attacked {opponent_pokemon_name}\n")
                              opponent_pokemon_value = pokedex[opponent_pokemon_name]
                              if opponent_pokemon_value['defense'] == 4 or opponent_pokemon_value["defense"] > 4:
                                    print(f"you attacked {opponent_pokemon_name} with max defense, you did no damage, resseting {opponent_pokemon_name}'s defense")
                                    opponent_pokemon_value["defense"] == 0
                              else:
                                    opponent_pokemon_value["health"] = opponent_pokemon_value["health"] - user_pokemon_value["damage"]
                              if opponent_pokemon_value["health"] == 0 or opponent_pokemon_value["health"] < 0:
                                    print("you won, congrats")
                                    money = money + 20
                                    print(f" you have now {money} dollars")
                                    break
                              print(f"your opponent,{opponent_pokemon_name}, has {opponent_pokemon_value['health']} health left \n")
                              print(f"{opponent_pokemon_name} will now go.\n")
                              opponent_attack = random.randint(1,2)
                              if opponent_attack == 1:
                                    opponent_pokemon_value["defense"] = opponent_pokemon_value["defense"] + 1
                                    if opponent_pokemon_value["defense"] == 4 or opponent_pokemon_value['defense'] > 4:
                                          opponent_pokemon_value == 4
                                    else:
                                          print(f"your opponent has {opponent_pokemon_value['defense']} defense level now")
                              elif opponent_attack == 2:
                                    if user_pokemon_value['defense'] == 4 or user_pokemon_value['defense'] > 4:
                                          print(f"You have maximum defense points, {opponent_pokemon_name} did no damage to you")
                                          user_pokemon_value['defense'] == 0
                                    else:
                                          user_pokemon_value['health'] = user_pokemon_value["health"] - opponent_pokemon_value["damage"]
                                          print(f"{opponent_pokemon_name} has attacked you have now {user_pokemon_value['health']} health left\n")
                                    if user_pokemon_value["health"] == 0 or user_pokemon_value["health"] < 0:
                                          print("you have lost")
                                          break
                              
                        
                        #defense mechanics
                  elif input_battle_1 == "2":
                              print(f"you defended your pokemon,{user_pokemon_name}.")
                              user_pokemon_value["defense"] = user_pokemon_value["defense"] + 1
                              if user_pokemon_value["defense"] == 4 or user_pokemon_value["defense"] > 4:
                                    print("you cannot increase defense, remember next time!")
                                    user_pokemon_value["defense"] == 4
                              else:
                                    print(f"your defense level is {user_pokemon_value['defense']}\n")
                              print(f"{opponent_pokemon_name} will now go.\n")
                              opponent_attack = random.randint(1,3)
                              if opponent_attack == 1:
                                    opponent_pokemon_value["defense"] = opponent_pokemon_value["defense"] + 1
                                    if opponent_pokemon_value["defense"] == 4 or opponent_pokemon_value['defense'] > 4:
                                          opponent_pokemon_value == 4
                                    else:
                                          print(f"your opponent has {opponent_pokemon_value['defense']} defense level now")
                              elif opponent_attack == 2:
                                    if user_pokemon_value['defense'] == 4 or user_pokemon_value['defense'] > 4:
                                          print(f"You have maximum defense points, {opponent_pokemon_name} did no damage to you")
                                          user_pokemon_value['defense'] == 0
                                    else:
                                          user_pokemon_value['health'] = opponent_pokemon_value["damage"]- user_pokemon_value['health']
                                          print(f"your {opponent_pokemon_name} has attacked you you have now {user_pokemon_value['health']}")
                                    if user_pokemon_value["health"] or user_pokemon_value["health"] < 0== 0:
                                          print("you have lost")
                                          break 
                                    else:
                                          print("you may go now")


      #shop
      if start_input == "2":
            print(f"hello welcome to the shop, you may buy pokemon here\n")
            shop_pokemon = {
                  "bulbasaur" : {"health": 30, "type": "grass","damage": 12,"defense":0,"price": 25},
                  "scorbunny" : {"health": 30, "type":"fire","damage": 12,"defense":0, "price" : 35},
                  "lobunny"  : {"health": 40,"type":"earth","damage":15,"defense":0,"price": 40},
                  "taillow" : {"health": 27,"type":"flying","damage":8,"defense":0,"price": 15},
                  "litten" : {"health": 35,"type":"fire","damage" : 13,"defense":0,"price": 20},
                  }
            for shop_key in shop_pokemon.keys():
             print(f"{shop_key}:{shop_pokemon[shop_key]}\n")

            bought_pokemon = input("what would you like to buy?(type exact way is spelt in list)\n")

            if bought_pokemon in shop_pokemon.keys():
                  bought_pokemon_stats = shop_pokemon[bought_pokemon]
                  if bought_pokemon_stats["price"] == money or bought_pokemon_stats["price"] < money:
                        pokedex[bought_pokemon] = bought_pokemon_stats
                        print(f"{bought_pokemon} was added to your pokedex!\n")
                        money - bought_pokemon_stats["price"]
                        print(f"you have now {money} dollars")
                  else:
                        print("insuficient money for pokemon!\n")      
              
        