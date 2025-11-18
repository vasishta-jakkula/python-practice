input_list_num = input(" pleas give 3 numbers seperated in spaces")
input_list_num = input_list_num.split()
list_num = []
for number in input_list_num:
    list_num.append(number)
total_sum = 0
total_multiply = 0
for number in list_num:
    total_sum += number
    total_multiply *= number
    print(total_sum,total_multiply)
