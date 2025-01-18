input_grade = input("give me a number of a grade(1 to 100) and see it in a alphabetical grade format!\n")
input_grade = int(input_grade)
if input_grade > 1 and input_grade < 21:
    print("F")
elif  input_grade > 21 and input_grade < 41:
    print("D")
elif input_grade > 41 and input_grade < 61:
    print("C")
elif input_grade > 61 and input_grade < 81:
    print("B")
elif input_grade > 81 and input_grade < 90:
    print("A")
elif input_grade > 90 and input_grade < 100:
    print("Excellent, you got an A+")
