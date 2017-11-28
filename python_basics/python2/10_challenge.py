f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
#print(rows[0:5])
int_crime_rates = []
for row in rows:
    crime_rate = row.split(',')
    print(crime_rate[1])
    int_crime_rates.append(int(crime_rate[1]))

print(int_crime_rates)
