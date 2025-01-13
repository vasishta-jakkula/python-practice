numbers = 24 
unit = "hours"

def days_to_units(days):
    return (f"{days} days are {days * numbers} {unit}")

user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")
user_input_number = int(user_input)
calaculated_value = days_to_units(user_input_number)
print(calaculated_value)
