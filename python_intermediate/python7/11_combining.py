import re

serious_start_count = 0
serious_end_count = 0
serious_count_final = 0
for post in posts:
    if re.search("^[\[\(][Ss]erious[\]\)]", post[0]):
        serious_start_count += 1
    if re.search("[\[\(][Ss]erious[\]\)]$", post[0]):
        serious_end_count += 1
    if re.search("^[\[\(][Ss]erious[\]\)]|[\[\(][Ss]erious[\]\)]$", post[0]):
        serious_count_final += 1
