def count_by_month(mon):
    month_count = 0
    for row in posts:
        if row[2].month == mon:
            month_count += 1
    return month_count

feb_count = count_by_month(2)
aug_count = count_by_month(8)
