def find_average(column):
    length = len(column)
    total = sum(column)
    return total / length

def find_length(column):
    length = len(column)
    return length

length = len(borrower_default_count_240)
average = find_average(principal_outstanding_240)
principal_length = find_length(principal_outstanding_240)
