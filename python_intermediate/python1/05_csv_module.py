import csv
f = open("nfl.csv")
nflreader = csv.reader(f)
nfl = list(nflreader)
