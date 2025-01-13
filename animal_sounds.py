unknown_sound = "i dont know what sound that animal makes try again!"

def animal_sound(animal):
    if animal == "cat":
        print("Meow!")
    elif animal == "dog":
        print("bark!")
    elif animal == "tiger":
        print("roar!")
    else:
        print(unknown_sound)
        
while True:
  input_sound = input("Give me a animal and I will say the sounds it makes!(only lowercase letters!)\n")
  animal_sound(input_sound)
