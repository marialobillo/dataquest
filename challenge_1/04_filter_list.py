# The last value is ~100 people
numerical_list[len(numerical_list)-1]
thousand_or_greater = []
for item in numerical_list:
    if item[1] >= 1000:
        thousand_or_greater.append(item[0])

for item in range(0,10):
    print(thousand_or_greater[item])
