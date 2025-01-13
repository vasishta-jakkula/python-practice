number =  12
input_value = input("tell me a number and i will multiply it by 12!\n")
if input_value.isdigit():
    print("hey you entered an integer string. I will covert to integer now")
    input_value = int(input_value)
# elif input_value.isfloat():
#     print("hey you entered an decimal string. I will covert to float now")
#     input_value = float(input_value)


def count(value):
    calculated_value = number * value
    print(f"{number} multiplied by {value} is {calculated_value}")

count(input_value)
