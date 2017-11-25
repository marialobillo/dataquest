f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
final_data = []
#print(rows[0:5])
for row in rows:
    split_data = row.split(',')
    final_data.append(split_data)

print(final_data[0:4])
