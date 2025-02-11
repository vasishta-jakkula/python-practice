while True:
    input_name = input("Hello player what would you like your name to be?\n")
    input_name_continue =  input(f"your name is {input_name} are you sure?(type y/n)\n")
    if input_name_continue == "y":
        choosing()
        break
    elif input_name_continue == "n":
        print('retrying now')
    else:
        print("invalid")

def choosing():
    print("hello!")