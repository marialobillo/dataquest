import numpy as np

world_alcohol = np.genfromtxt("world_alcohol.csv", delimiter=",", dtype="U75", skip_header=1)

print(world_alcohol)
