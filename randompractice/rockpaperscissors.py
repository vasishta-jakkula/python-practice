import random
print("Hello welcome to rock,paper,scissors!(PYTHON EDITION)\n")
input_start =input("(TYPE y OR n) would you like to play?\n")
if input_start == "y":
    print("let us begin")

    #game of rock paper scissors
    input_pick = input("What will you pick?(type exactly as shown)\n rock \n paper \n scissors \n")
    if input_pick == "rock":
        rps_ai = random.randint(1,3)
        if rps_ai == 1:
            print("Your opponent picked rock")
            if input_pick == "rock":
                print(" The game is a tie")
            if input_pick == "paper":
                print("You have won!")
            if input_pick == "scissors":
                print("Your opponent won!")
        if rps_ai == 2:
            print("Your opponent picked paper")
            if input_pick == "rock":
                print("Your opponent has won!")
            if input_pick == "paper":
                print("The game is a tie!")
            if input_pick == "scissors":
                print("You have won!")
        if rps_ai == 3:
            print("Your opponent picked scissors")
            if input_pick == "rock":
                print(" Your opponent won")
            if input_pick == "paper":
                print("You have won!")
            if input_pick == "scissors":
                print(" The game is a tie!")


    if input_pick == "paper":
        rps_ai = random.randint(1,3)
        if rps_ai == 1:
            print("Your opponent picked rock")
            if input_pick == "rock":
                print(" The game is a tie")
            if input_pick == "paper":
                print("You have won!")
            if input_pick == "scissors":
                print("Your opponent won!")
        if rps_ai == 2:
            print("Your opponent picked paper")
            if input_pick == "rock":
                print(" You have won!")
            if input_pick == "paper":
                print("The game is a tie!")
            if input_pick == "scissors":
                print("You oppoenet has won!")
    if rps_ai == 3:
        print("Your opponent picked scissors")
        if input_pick == "rock":
            print(" Your opponent won")
        if input_pick == "paper":
            print("You have won!")
        if input_pick == "scissors":
            print(" The game is a tie!")


    if input_pick == "scissors":
        rps_ai = random.randint(1,3)
        if rps_ai == 1:
            print("Your opponent picked rock")
            if input_pick == "rock":
                print(" The game is a tie")
            if input_pick == "paper":
                print("You have won!")
            if input_pick == "scissors":
                print("Your opponent won!")
        if rps_ai == 2:
            print("Your opponent picked paper")
            if input_pick == "rock":
                print(" You have won!")
            if input_pick == "paper":
                print("The game is a tie!")
            if input_pick == "scissors":
                print("You oppoenet has won!")
        if rps_ai == 3:
            print("Your opponent picked scissors")
            if input_pick == "rock":
                print(" Your opponent won")
            if input_pick == "paper":
                print("You have won!")
            if input_pick == "scissors":
                print(" The game is a tie!")


elif input_start == "n":
    print("ok i quit!")
else:
    print("invalid input retry!")



# code for AI guess
