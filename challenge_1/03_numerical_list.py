print(nested_list[0:5])
numerical_list = []
for item in nested_list:
    name = item[0]
    number = float(item[1])
    numerical_list.append([name, number])
​
for item in range(0,5):
    first_five.append(numerical_list[item])
