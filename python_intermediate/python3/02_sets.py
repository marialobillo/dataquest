gender = []
for row in legislators:
    gender.append(row[3])
gender = (set(gender))
print(gender)
