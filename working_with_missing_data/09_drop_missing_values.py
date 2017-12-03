

drop_na_columns = titanic_survival_dropna(axis=1)
new_titanic_survival = titanic_survival.dropna(axis=0, subset=["age", "sex"])
