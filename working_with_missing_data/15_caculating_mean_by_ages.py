import numpy as np
age_group_survival = titanic_survival.pivot_table(index="age_labels", values="survived")
