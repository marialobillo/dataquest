weighted_protein = food_info["Protein_(g)"] * 2

weighted_fat = food_info["Lipid_Tot_(g)"] * (-0.75)

initial_rating = weighted_protein + weighted_fat
