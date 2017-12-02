print("Rows 3, 4, 5 and 6")
print(food_info.loc[3:6])

print("Rows 2, 5, and 10")
two_five_ten = [2,5,10]
print(food_info.loc[two_five_ten])

total_rows = food_info.shape[0]
last_rows = food_info.loc[total_rows-5:total_rows-1]
