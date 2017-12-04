import pandas as pd

all_ages = pd.read_csv("all-ages.csv")
recent_grads = pd.read_csv("recent-grads.csv")

print(all_ages.iloc[0:5])
print(recent_grads.iloc[0:5])
