file = open('movie_metadata.csv')
movies = file.read()
movie_rows = movies.split('\n')
movie_data = []

for item in movie_rows:
    data = item.split(',')
    movie_data.append(data)

for item in range(0,5):
    print(movie_data[item])
