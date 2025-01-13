def day_to_hours(value):
    print(f"{value} days is {value * 24} hours!")


def negative_check(negative_input):
    negative_message = "you entered a negative number, so no conversion for you!"
    try:
     input_value = int(negative_input)
     if input_value < 0:
        print (negative_message)
     else:
      day_to_hours(negative_input)
    except:
     print(message)
message ="you entered a invalid number dont ruin my program!"
input_value = ""


while input_value != "exit":
 try:
  input_value = input ("Hey user give me a number of days and i will convert it to hours!\n")
  if input_value == "exit":
    break
  for num_of_hours in input_value.split(","):
   """if num_of_hours == "exit":
     break"""
   num_of_hours = int(num_of_hours)
   negative_check(num_of_hours)
 except:
  print(message)
