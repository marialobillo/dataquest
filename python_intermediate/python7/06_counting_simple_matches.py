import re

of_reddit_count = 0
for post in posts:
    if re.search('of Reddit',post[0]):
        of_reddit_count += 1

print(of_reddit_count)
