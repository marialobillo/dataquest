print(food_info["Protein_(g)"][0:5])
max_protein = food_info["Protein_(g)"].max()

normalized_protein = food_info["Protein_(g)"] / max_protein

max_fat = food_info["Lipid_Tot_(g)"].max()
normalized_fat = food_info["Lipid_Tot_(g)"] / max_fat
