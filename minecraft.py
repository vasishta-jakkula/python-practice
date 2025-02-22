from random import *
village_made = False
exploration_level = 0
village_level = 0
crafting_level = 0
wood = 0
food = 0
stone = 0
diamonds = 0
emeralds = 0
gold = 0

print("welcome to minecraft!\n")
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
input1 = input("would you like to make an village here if so type 1\n If you want to gather materials type 2\n if you want to check inventory type 3\n if you quit type 4\n")

    #village make
if input1 == "1":
        input_village_name = input("starting settlement, what will you call it?")
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
            if random_resources == 2:
                wood = wood + 3
                stone = stone + 4
            if random_resources == 3:
                wood = wood + 2
                stone = stone + 8
            if random_resources == 4:
                wood = wood + 5
                stone = stone +3
            if random_resources == 5:
                wood = wood + 5
                stone = stone + 5
        if exploration_level == 1:
            print("you can only gather wood,stone,and gold")
        if exploration_level == 2:
            print("you can only gather wood,stone,gold, and emeralds")
        if exploration_level == 3:
            print("you can only gather wood,stone,gold,emeralds, and diamonds")
        
        


if input1 == "3":
        print("h")


if input1 == "4":
        print("we will now quit the program")
        quit()