age_is_null = pd.isnull(titanic_survival["age"])
good_ages = titanic_survival["age"][age_is_null == False]
correct_mean_age = sum(good_ages) / len(good_ages)
