def feature_counter(input_lst,index, input_str, header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        if each[index] == input_str:
            num_elt = num_elt + 1
    return num_elt
def summary_statistics(input_list):
    num_japan_films = feature_counter(movie_data, 6, "Japan", False
                                     )
    num_color_films = feature_counter(movie_data, 2, "Color", True )
    num_films_in_english = feature_counter(movie_data, 5, "English", True )
    print(num_japan_films)
    summary = {
        "japan_films": num_japan_films,
        "color_films": num_color_films,
        "films_in_english": num_films_in_english
    }
    return summary

summary = {}
summary = summary_statistics(movie_data)
