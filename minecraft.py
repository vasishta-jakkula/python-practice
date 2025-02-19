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
if input1 == 1:
    input_village_name = input("starting settlement, what will you call it?")
    input_village_name_check = input_village_name
if input1 == 2:
    print("h")
if input1 == 3:
    print("h")
if input1 == 4:
    print("we will now quit the program")
    # break a while loop 