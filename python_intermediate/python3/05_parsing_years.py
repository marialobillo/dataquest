birth_years = []
for row in legislators:
    parts = row[2].split('-')
    birth_years.append(parts[0])

print(birth_years)
