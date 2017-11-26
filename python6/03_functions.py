def get_names(movie_data):
    movie_name = []
    for item in movie_data:
        movie_name.append(item[0])
    return movie_name

movie_names = []
movie_names = get_names(movie_data)
for item in range(1,6):
    print(movie_names[item])
