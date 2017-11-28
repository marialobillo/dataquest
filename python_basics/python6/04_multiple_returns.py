wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def is_usa(movie):
    if movie[6].lower() == 'usa':
        return True
    else:
        return False

wonder_woman_usa = is_usa(wonder_woman)
