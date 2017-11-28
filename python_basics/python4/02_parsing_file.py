file = open('la_weather.csv')
data = file.read()
data_rows = data.split('\n')
#print(data_rows)
weather_data = []
for item in data_rows:
    day_row = item.split(',')
    print(day_row)
    weather_data.append(day_row)å
