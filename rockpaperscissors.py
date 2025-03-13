import random
print("Hello welcome to rock,paper,scissors!(PYTHON EDITION)\n")
input_start =input("(TYPE Y OR N) would you like to play?\n")
if input_start == "y":
    print("let us begin")

    #game of rock paper scissors
    input_pick = input("What will you pick?(type exactly as shown)\n rock \n paper \n scissors \n")
    if input_pick == "rock":
        print("R")
    if input_pick == "paper":
        print("P")
    if input_pick == "scissors":
        print("S")    
elif input_start == "n":
    print("ok i quit!")
else:
    print("invalid input retry!")



# code for AI guess
rps_ai = random.randint(1,3)
if rps_ai == 1:
    print("Your opponent picked rock")