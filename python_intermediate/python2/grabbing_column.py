# Default display code
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]

    def column(self, label):
        if label not in self.header:
            return None
        for idx, value in enumerate(self.header):
            if label == value:
                index = idx
        column = []
        for row in self.data:
            column.append(row[index])
        return column

    # Add your method here.

nfl_dataset = Dataset(nfl_data)
year_column = nfl_dataset.column('year')
player_column = nfl_dataset.column('player')
