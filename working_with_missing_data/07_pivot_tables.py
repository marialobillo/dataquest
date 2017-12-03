passenger_survival = titanic_survival.pivot_table(index="pclass", values="survived")
passenger_age = titanic_survival.pivot_table(index="pclass", values="age")
