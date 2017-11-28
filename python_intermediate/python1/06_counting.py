import csv
f = open("nfl.csv", "r")
nfl = list(csv.reader(f))
patriots_wins = 0
for winner in nfl:
    if winner[2] == 'New England Patriots':
       patriots_wins += 1
