pantry = ["apple", "orange", "grape", "apple", "orange", "apple", "tomato", "potato", "grape"]
pantry_counts = {}
for fruit in pantry:
    if fruit in pantry_counts:
        pantry_counts[fruit] += 1
    else:
        pantry_counts[fruit] = 1
