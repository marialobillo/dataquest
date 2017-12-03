import numpy as np

port_stats = titanic_survival.pivot_table(index="embarked", values=["fare", "survived"],aggfunc=np.sum)

print(port_stats)
