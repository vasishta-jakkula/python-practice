import random
village_made = False
exploration_level = 0
village_level = 0
crafting_level = 0
crafting_table = 0
village_npc_num = 0
wood = 0
food = 0
stone = 0
diamonds = 0
emeralds = 0
gold = 0

print("welcome to minecraft!\n")
print("current update (1.0: The begining!)\n")
#for name check
while True:
    input_name = input("what will be you name?(must be less than 10 letters)\n")
    input_name_check = len(input_name)
    if input_name_check > 10 or input_name_check == 10:
        print("name is too long, try again")
    elif input_name_check == 0:
        print("no letters in name")
    else:
        break
print(f"Your name is {input_name}")
print("you have a wooden sword, and wooden pick in you inventory.\n")
input1 = input("would you like to make an village here if so type 1\n If you want to gather materials type 2\n if you quit type 3\n")

    #village make
if input1 == "1":
        input_village_name = input("starting settlement, what will you call it?\n")
        input_village_name_check = input_village_name
        if len(input_village_name_check) == 0:
            print("you village has no letters, try again.")
        else:
            print(f"you created a new village,{input_village_name}")
            village_made = True
            village_level = village_level + 1

random_resources = ""        
if input1 == "2":
        print("you decided to gather materials")
        if exploration_level == 0:
            print("you can only gather wood, and stone")
            random_resources = random.randint(1,5)
            if random_resources == 1:
                wood = wood + 4
                stone = stone +6
            elif random_resources == 2:
                wood = wood + 3
                stone = stone + 4
            elif random_resources == 3:
                wood = wood + 2
                stone = stone + 8
            elif random_resources == 4:
                wood = wood + 5
                stone = stone +3
            elif random_resources == 5:
                wood = wood + 5
                stone = stone + 5
            print("your resources are gathered")
        if exploration_level == 1:
            print("you can only gather wood,stone,and gold")
            random_resources = random.randint(1,5)
            if random_resources == 1:
                wood = wood + 4
                stone = stone +6
            elif random_resources == 2:
                wood = wood + 3
                stone = stone + 4
            elif random_resources == 3:
                wood = wood + 2
                stone = stone + 8
            elif random_resources == 4:
                wood = wood + 5
                stone = stone +3
            elif random_resources == 5:
                wood = wood + 5
                stone = stone + 5
        if exploration_level == 2:
            print("you can only gather wood,stone,gold, and emeralds")
            random_resources = random.randint(1,5)
            if random_resources == 1:
                wood = wood + 4
                stone = stone +6
                gold = gold +1
            elif random_resources == 2:
                wood = wood + 2
                stone = stone + 4
                gold = gold +2
                emeralds = emeralds + 2
            elif random_resources == 3:
                wood = wood + 2
                stone = stone + 8
                gold = gold + 0
                emeralds = emeralds + 3
            elif random_resources == 4:
                wood = wood + 5
                stone = stone +3
                gold = gold + 3
                emeralds = emeralds + 1
            elif random_resources == 5:
                wood = wood + 5
                stone = stone + 5
                gold = gold + 1
                emeralds =  emeralds + 3
        if exploration_level == 3:
            print("you can only gather wood,stone,gold,emeralds, and diamonds")
            random_resources = random.randint(1,5)

            if random_resources == 1:
                wood = wood + 10
                stone = stone +8
                gold = gold +3
                diamonds= diamonds + 1
                emeralds = emeralds + 3

            elif random_resources == 2:
                wood = wood + 9 
                stone = stone + 11
                gold = gold +4
                diamonds = diamonds + 3
                emeralds = emeralds + 5 

            elif random_resources == 3:
                wood = wood + 7
                stone = stone + 8
                gold = gold + 5
                emeralds = emeralds + 3
                diamonds = diamonds + 2

            elif random_resources == 4:
                wood = wood + 7
                stone = stone +5
                gold = gold + 8
                emeralds = emeralds + 9
                diamonds = diamonds + 4

            elif random_resources == 5:
                wood = wood + 5
                stone = stone + 5
                gold = gold + 4
                emeralds =  emeralds + 7
                diamonds = diamonds + 3

elif input1 == "3":
        print("we will now quit the program")
        quit()

print("You have begun!")
input2 = input("what will you do? 1. village settings, 2. explore, 3. craft")

if input2 == "1":
    print("let's check if you have a village first")
    if village_made == True:
        print("you have a village! Lets check it out")
    elif village_made == False:
        print("you dont have a village let's make one!")
        input_village_name = input("starting settlement, what will you call it?\n")
        input_village_name_check = input_village_name
        if len(input_village_name_check) == 0:
            print("you village has no letters, try again.\n")
        else:
            print(f"you created a new village,{input_village_name}\n")
            village_made = True
            village_level = village_level + 1
    
    input_village_choices = input(" what will you do? 1. check settings, 2. upgrade village, 3. collect NPC's for jobs\n")
    if input_village_choices == "1":
        print(f"lets check settings\n")
        input_village_settings = input("pick one of 3 settings, 1. check status, 2. remove village, 3. leave settings")
        if input_village_settings == "1":
            print(f"your village stats\n the number of npc's in village are {village_npc_num}\n village level is{village_level}\n")
    if input_village_choices == "2":
        input_continue_1 = input("are you sure?")

if input2 == "2":
    print("you decided to gather materials")
    if exploration_level == 0:
            print("you can only gather wood, and stone")
            random_resources = random.randint(1,5)
            if random_resources == 1:
                wood = wood + 4
                stone = stone +6
            elif random_resources == 2:
                wood = wood + 3
                stone = stone + 4
            elif random_resources == 3:
                wood = wood + 2
                stone = stone + 8
            elif random_resources == 4:
                wood = wood + 5
                stone = stone +3
            elif random_resources == 5:
                wood = wood + 5
                stone = stone + 5
            print("your resources are gathered")
            if exploration_level == 1:
                print("you can only gather wood,stone,and gold")
                random_resources = random.randint(1,5)
                if random_resources == 1:
                    wood = wood + 4
                    stone = stone +6
                elif random_resources == 2:
                    wood = wood + 3
                    stone = stone + 4
                elif random_resources == 3:
                    wood = wood + 2
                    stone = stone + 8
                elif random_resources == 4:
                    wood = wood + 5
                    stone = stone +3
                elif random_resources == 5:
                    wood = wood + 5
                    stone = stone + 5
            if exploration_level == 2:
                print("you can only gather wood,stone,gold, and emeralds")
                random_resources = random.randint(1,5)
                if random_resources == 1:
                    wood = wood + 4
                    stone = stone +6
                    gold = gold +1
                elif random_resources == 2:
                    wood = wood + 2
                    stone = stone + 4
                    gold = gold +2
                    emeralds = emeralds + 2
                elif random_resources == 3:
                    wood = wood + 2
                    stone = stone + 8
                    gold = gold + 0
                    emeralds = emeralds + 3
                elif random_resources == 4:
                    wood = wood + 5
                    stone = stone +3
                    gold = gold + 3
                    emeralds = emeralds + 1
                elif random_resources == 5:
                    wood = wood + 5
                    stone = stone + 5
                    gold = gold + 1
                    emeralds =  emeralds + 3
            if exploration_level == 3:
                print("you can only gather wood,stone,gold,emeralds, and diamonds")
                random_resources = random.randint(1,5)

                if random_resources == 1:
                    wood = wood + 10
                    stone = stone +8
                    gold = gold +3
                    diamonds= diamonds + 1
                    emeralds = emeralds + 3

                elif random_resources == 2:
                    wood = wood + 9 
                    stone = stone + 11
                    gold = gold +4
                    diamonds = diamonds + 3
                    emeralds = emeralds + 5 

                elif random_resources == 3:
                    wood = wood + 7
                    stone = stone + 8
                    gold = gold + 5
                    emeralds = emeralds + 3
                    diamonds = diamonds + 2

                elif random_resources == 4:
                    wood = wood + 7
                    stone = stone +5
                    gold = gold + 8
                    emeralds = emeralds + 9
                    diamonds = diamonds + 4

                elif random_resources == 5:
                    wood = wood + 5
                    stone = stone + 5
                    gold = gold + 4
                    emeralds =  emeralds + 7
                    diamonds = diamonds + 3


if input2 == "3":
    print('in progress')