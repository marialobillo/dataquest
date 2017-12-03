max_protein = food_info["Protein_(g)"].max()

normalized_protein = food_info["Protein_(g)"] / max_protein

food_info["Normalized_Protein"] = normalized_protein

food_info["Normalized_Fat"] = normalized_fat

#as a dictionary
