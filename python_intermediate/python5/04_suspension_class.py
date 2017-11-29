class Suspension:
    def __init__(self, data):
        self.data = data
        self.name = data[0]
        self.team = data[1]
        self.games = data[2]
        self.year = data[5]

third_suspension = Suspension(nfl_suspensions[2])
