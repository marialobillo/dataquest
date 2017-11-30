import datetime

for post in posts:
    post[2] = datetime.datetime.fromtimestamp(float(post[2]))
