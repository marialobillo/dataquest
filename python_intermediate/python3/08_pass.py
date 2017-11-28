converted_years = []
for year in birth_years:
    try:
        year = int(year)
    except Exception:
        pass
    converted_years.append(year)
   
