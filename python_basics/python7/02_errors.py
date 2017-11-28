def first_elts (input_lst):
    elts = []
    for each in input_lst:
        elts.append(each[0])
    return elts

animals = [["dog","cat","rabbit"],["turtle","snake"],["sloth","penguin","bird"]]
first_animal = first_elts(animals)
print(first_animal)
