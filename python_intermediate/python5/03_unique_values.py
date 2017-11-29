unique_teams = []
for row in nfl_suspensions:
    team = row[1]
    if team not in unique_teams:
        unique_teams.append(team)
unique_teams = set(unique_teams)
unique_games = []
for row in nfl_suspensions:
    game = row[2]
    if game not in unique_games:
        unique_games.append(game)
unique_games = set(unique_games)

  
