#print(food_info.head(2))
columns = food_info.columns.tolist()
#print(columns)
ending = "(g)"
gram_columns = []
for each in columns:
    if each.endswith(ending):
        gram_columns.append(each)

print(gram_columns)

gram_df = food_info[gram_columns]
