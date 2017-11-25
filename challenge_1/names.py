f = open('dq_unisex_names.csv', 'r')
names = f.read()
first_five = []
names_list = names.split('\n')
for item in range(0,5):

    first_five.append(names_list[item])


print(first_five)
