water_energy = food_info["Water_(g)"] * food_info["Energ_Kcal"]
print(water_energy[0:5])

grams_of_protein_per_gram_of_water = food_info["Protein_(g)"] / food_info["Water_(g)"]

milligrams_of_calcium_and_iron = food_info["Calcium_(mg)"] + food_info["Iron_(mg)"]
