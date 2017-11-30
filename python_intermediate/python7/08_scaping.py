import re

serious_count = 0
for post in posts:
    if re.search("\[Serious\]", post[0]):
        serious_count += 1
