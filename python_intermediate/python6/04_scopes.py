def find_average(column):
    length = len(column)
    total = sum(column)
    return total / length

total = sum(borrower_default_count_240)
average = find_average(principal_outstanding_240)
print(total)
