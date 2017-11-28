import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

def nfl_wins(team):
    team_wins = 0
    for winner in nfl:
        if winner[2] == team:
            team_wins += 1
    return team_wins
cowboys_wins = nfl_wins("Dallas Cowboys")
falcons_wins = nfl_wins("Atlanta Falcons")
