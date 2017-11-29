class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        try:
            self.year = int(row[5])
        except Exception:
            self.year = 0
    def get_year(self):
        return(self.year)


missing_year = Suspension(nfl_suspensions[22])
twenty_third_year = missing_year.get_year()
