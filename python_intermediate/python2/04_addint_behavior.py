# Default display code
class Dataset:
    def __init__(self, data):
        self.data = data

    # Your method goes here
    def print_data(self, num_rows):
        print(self.data[:num_rows])

nfl_data = Dataset(nfl_data)
nfl_data.print_data(5)
