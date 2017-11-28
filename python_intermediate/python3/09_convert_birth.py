for row in legislators:
    parts = row[2].split('-')
    try:
        birth_year = int(parts[0])
    except Exception:
        birth_year = 0
    row.append(birth_year)
