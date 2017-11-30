import csv
f = open('askreddit_2015.csv', 'r')
data = csv.reader(f)
posts_with_header = list(data)
posts = posts_with_header[1:]
for post in posts[:10]:
    print(post)
