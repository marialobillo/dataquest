import re

year_strings = []
for each in strings:
    if re.search("[1-2][0-9]{3}", each) is not None:
        year_strings.append(each)
