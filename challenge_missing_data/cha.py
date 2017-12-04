import pandas as pd

all_ages = pd.read_csv("all-ages.csv")
recent_grads = pd.read_csv("recent-grads.csv")

#print(all_ages.iloc[0:5])
#print("==============================================")
#print(recent_grads.iloc[0:5])

columns = all_ages["Mayor_category", "Total"]

columns_selected = all_ages[columns]
print(columns_selected.iloc[0:8])
