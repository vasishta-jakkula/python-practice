def input_statement(num):
    finished_text = f"the calaculation for the {num} and the numbers before is "
    if input_number == 0:
        print ("You entered a zero, so no conversion for you!")
    else:
        sum = 0
        
        for count in range(1,input_number + 1):
            sum = sum + count 
        print(sum)
input_number = ""
while input_number != "exit":
   if input_number == "exit":
    quit()
   try:
    input_number = input("give me number and I will add the sum of all the numbers before it to that number.\n")
    input_number = int(input_number)
    input_statement(input_number)
   except Exception as E:
      print(E)
      print("don ruin my program pls")
