input_grade = input("give me a number of a grade(1 to 100) and see it in a alphabetical grade format!\n")
input_grade = int(input_grade)
if input_grade > 1 and input_grade < 21:
    print("F")
elif  input_grade > 21 and input_grade < 40:
    print("E")
