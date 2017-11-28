class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
    def column(self, label):
        if label not in self.header:
            return None
        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx
        column = []
        for row in self.data:
            column.append(row[index])
        return column

    def count_unique(self, label):
        results = set(self.column(label))
        return len(results)
    # Add your count unique method here
nfl_dataset = Dataset(nfl_data)
total_years = nfl_dataset.count_unique('year')
