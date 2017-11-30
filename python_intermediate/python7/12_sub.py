import re


for post in posts:
    post[0] = re.sub("[\[\(][Ss]erious[\]\)]", "[Serious]", post[0])
