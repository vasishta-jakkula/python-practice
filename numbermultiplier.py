input_value = input ("Hey user give me a number of days and i will convert it to hours!\n")

def day_to_hours(value):
    print(f"{value} days is {value * 24} hours!")


def negative_check(negative_input):
    negative_message = "you entered a negative number, so no conversion for you!"
    if input_value < 0:
        print (negative_message)
    else:
        day_to_hours(negative_input)
try:
  input_value = int(input_value)
  negative_check(input_value)
except:

    print("you entered an invalid number, please try again(no decimals allowed).")





    
