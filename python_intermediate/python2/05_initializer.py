# Default display code
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]


nfl_dataset = Dataset(nfl_data)
nfl_header = nfl_dataset.header
