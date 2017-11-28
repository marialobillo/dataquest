
class Dataset:
    def __init__(self, data):
        self.data = data

f = open("nfl.csv")
csvreader = csv.reader(f)
nfl_data = list(csvreader)
nfl_dataset = Dataset(nfl_data)
dataset_data = nfl_dataset.data
