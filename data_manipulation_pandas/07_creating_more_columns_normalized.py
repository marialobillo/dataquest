food_info["Normalized_Protein"] = food_info["Protein_(g)"] / food_info["Protein_(g)"].max()
food_info["Normalized_Fat"] = food_info["Lipid_Tot_(g)"] / food_info["Lipid_Tot_(g)"].max()

protein = 2 * food_info["Normalized_Protein"]
fat = 0.75 * food_info["Normalized_Fat"]
food_info["Norm_Nutr_Index"] = protein - fat
