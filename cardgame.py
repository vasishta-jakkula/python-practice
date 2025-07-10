import random
opponent_kit_random = "1"
opponent1_kit = {"energypoints": 0,"HyperChargeBoolean": False,}
opponent2_kit = {"energypoints": 0,"HyperChargeBoolean": False,}
opponent3_kit = {"energypoints": 0,"HyperChargeBoolean": False,}
kit = {"energypoints": 0,"HyperChargeBoolean": False,}
print(" Welcome to Fighting(PYTHON EDITION) version 1.0")
input_kit_user = input(" Type the number of the kit you want to use,\n 1. CLOWN 2. WARRIOR 3. WIZARD 4. AQUMAN\n")
if input_kit_user == "1":
    kit["Trickery"] = 20
    kit["Jester Jingles"] = 30
    kit["Rising Hammer(SUPER)"] = 60
    print(" Your moves are \nTrickery = 20dmg and 2 energy needed \nJester Jingles = 30dmg and 4 energy needed\nRising Hammer= 60dmg and 7 energy needed")
else:
    print(" Invalid Number Try again ")

input_num_of_people = input("How many people do you want to play with? (max 3)")
if input_num_of_people == "1":
    print("You have one opponent\n")
    #opponent_kit_random = random.randint(1,5)
    opponent_kit_random = 1
    if opponent_kit_random == 1:
        print("Your opponents Kit is CLOWN:")
        opponent1_kit["Trickery"] = 20
        opponent1_kit["Jester Jingles"] = 30
        opponent1_kit["Rising Hammer(SUPER)"] = 60
        print(" Your opponents moves are \nTrickery = 20dmg and 2 energy needed \nJester Jingles = 30dmg and 4 energy needed\nRising Hammer= 60dmg and 7 energy needed\n")
    if opponent_kit_random == 2:
        pass
    if opponent_kit_random == 3:
        pass
    if opponent_kit_random == 4:
        pass
if input_num_of_people == "2":
    print(" You have Two opponents")
if input_num_of_people == "3":
    print("You have Three opponents")

print("Begin The Battle!")


