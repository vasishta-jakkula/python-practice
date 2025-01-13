#global Variables
numbers = 24 * 60 * 60
unit = "seconds"

#Variables named in function are local variables, cannot be shared outside only specific to the function.
def days_to_units(days, custom_message):
    print(f"{days} days are {days * numbers} {unit}")
    print(custom_message)
    
def scope_check():
     my_var = "hello"
     print(numbers)
     print(unit)
     print(my_var)

days_to_units(20, " awesome!!")
