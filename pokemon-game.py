def choosing():
    input_pick = input("pick a thing to do,(type number)\n1. go to pokedex to pick pokemon\n2. check your rank\n3. fight/play\n")
    if input_pick == "1":
        print("h")
    elif input_pick == "2":
        print("h")
    elif input_pick == "3":
        print("h")
while True:
    input_name = input("Hello player what would you like your name to be?\n")
    input_name_continue =  input(f"your name is {input_name} are you sure?(type y/n)\n")
    if input_name_continue == "y":
        choosing()
        break
    elif input_name_continue == "n":
        print('retrying now')
    else:
        print("invalid")

pikachu = {"type":"electric","damage":7,"health":30}
eevee = {"type":"normal","damage":7,"health":30}
