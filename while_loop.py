
def number_of_years(years):
    print(f"{years} is {years * 365} days!")

def number_of_days(input_value):
    zero_message = "you entered a zero so there will be no conversion for you!"
    negative_message = " you entered a negative number the will be no conversion for you!"
    if input_value == 0:
        print(zero_message)
    elif input_value < 0:
        print(negative_message)
    else:
        number_of_years(input_value)
while True:
    try:
     input_value_years = input("Hello, enter a number of years and I will transfer it to the number of days!\n")
     input_value_years =  int(input_value_years)
     number_of_days(input_value_years)
    except:
            print("you entered an invalid number, please try again!")
       # Exception as E (used to check for errors after except then print the vairable which is "E" in this case

