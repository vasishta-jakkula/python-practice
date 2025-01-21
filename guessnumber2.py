import random
random_number = random.randint(1,20)
number_of_attempts = 0
while True:
 try:
    input_value = input("guess a number from zero to one-hundred and see if you can get it.\n")
    number_of_attempts = number_of_attempts + 1
    input_value = int(input_value)
    if number_of_attempts == 7:
       print("too many attempts rerun the program!")
       break
    if input_value == random_number:
        print("you guessed it!")
        break
    if input_value > random_number:
        print("too high!")
    if input_value < random_number:
       print("too low")
 except:
    print("invalid  guess")
