party = []
for row in legislators:
    party.append(row[6])
party = set(party)
print(party)
