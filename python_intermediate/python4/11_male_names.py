top_male_names = []
male_name_counts = {}
count = 0
for row in legislators:
    if row[3] == 'M' and row[7] > 1940:
        name = row[1]
        if name in male_name_counts:
            male_name_counts[name] += 1
        else:
            male_name_counts[name] = 1
max_value = None
for row in male_name_counts:
    count = male_name_counts[row]
    if max_value is None or count > max_value:
        max_value = count
for key, value in male_name_counts.items():
    if value >= max_value:
        top_male_names.append(key)
