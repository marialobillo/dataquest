crime_rates = []
cities_list = []
for row in five_elements:
    # row is a list variable, not a string.
    crime_rate = row[1]
    # crime_rate is a string, the crime rate of the city.
    crime_rates.append(crime_rate)

for row in final_data:
    city_name = row[0]
    cities_list.append(city_name)
