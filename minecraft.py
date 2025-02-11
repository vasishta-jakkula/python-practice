while True:
    input_player_chose =input("pick between steve or alex as your main character in this adventure!(keep in lower case and exact or it wont run!).\n")
    if input_player_chose == "steve":
        input_continue_steve = input("You chose Steve as your character, would you like to confirm,say yes or no.\n")
        if input_continue_steve  == "yes":
            from steve_play import *
            print("\n")
            print("\n")
            steve_play()
            break
        else:
            print("try again")
    
    elif input_player_chose == "alex":
        input_continue_alex = input ("You chose Alex as your character, would you like to confirm, say yes or no.\n")
        if input_continue_alex == "yes":
            print("Alex story isnt here yet try steve")
            break
        else:
            print("try again")
    else:
        print("try again")



