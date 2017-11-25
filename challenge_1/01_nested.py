f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')
nested_list = []
for item in names_list:
    comma_list = item.split(',')
    nested_list.append(comma_list)

print(nested_list)
