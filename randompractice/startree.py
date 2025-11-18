# input_num = input("give me a number and it will make a tree of stars!\n")
input_num = "8"
try:
    input_num = int(input_num)
    for row in range(1,input_num+1):
        print(" ><|>" * row)
except:
    print("invalid input")
