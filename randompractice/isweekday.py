def is_week_day(user_input_day):
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    week_ends = ["Sunday", "Saturday"]
    # if user_input_day == "Sunday" or user_input_day == "Saturday":
    if user_input_day in week_ends:
        return "Weekend"
    if user_input_day in week_days:
        return "Week Day"
    return "Not a week day or weekend"

def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"

def is_divisiable_by_7(number):
    if number % 7 == 0:
        return "Yes"
    return "No"

# user_input = input("Hey, enter a day to check if its weekday or weekend?\n")
# value = is_week_day(user_input)
# print(value)

# user_input = input("Enter a number. I will tell you if its Even or Odd?\n")
# value = is_even_or_odd(int(user_input))
# print(value)

user_input = input("Enter a number. I will tell you if its divisible by 7?\n")
value = is_divisiable_by_7(int(user_input))
print(value)

