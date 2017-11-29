max_value = None
for row in name_counts:
    count = name_counts[row]
    if max_value is None or count > max_value:
        max_value = count

print(max_value)
