print("welcome to minecraft!\n")
while True:
    input_name = input("what will be you name?(must be less than 10 letters)\n")
    input_name_check = len(input_name)
    if input_name_check > 10 or input_name_check == 10:
        print("name is too long, try again")
    elif input_name_check == 0:
        print("no letters in name")
    else:
        break
print("YYYY")
