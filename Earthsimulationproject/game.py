#imports
import random
import Catastophe

# variables
money = 1000
properties = {}
age=0
criminal_history_level = 0
job = ""
salary = 0
credit_score = 0
items = []
passcode = 0
dead = False
disaster = False
cancer = False

input_name=input("Hello, What will your name be?____")
print(f"Welcome {input_name}, have fun and try to survive.")

while disaster != True:
    if dead == True:
        print("game over, retry")
        quit()
    input_player_choice = input(f"(you are {age} years old (Type the num) 1. Age by 1 ,2. check stats, 3. find a job(needs to be 18 age)")
    if input_player_choice == '1':
        print(f"You are now {age} years old, congrats")
        cancer_wheel = random.randint(1,500)
        if cancer_wheel == 15 or cancer_wheel == 32 or cancer_wheel == 56:
            print("you have been diagnosed with cancer,sorry")
        if age == 13 and cancer == True:
            print("you died to cancer")
            dead= True
        if age <= 32:
            print(f"A world catastrophe has happened, and it is {Catastophe.disasters}, survive")
    if input_player_choice == "2":
        print(f'Here are your stats\nmoney = {money}\nproperties owned{properties}\nage = {age}\ncriminalhistorylevel = {criminal_history_level}\n job = {job}\nsalary = {salary}')