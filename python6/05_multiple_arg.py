wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def is_usa(input_lst):
    if input_lst[6] == "USA":
        return True
    else:
        return False
def index_equals_str(input_list, index, argument):
    if input_list[index] == argument:
        return True
    else:
        return False
wonder_woman_in_color = index_equals_str(wonder_woman, 2, 'Color')
