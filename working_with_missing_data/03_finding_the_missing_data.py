age = titanic_survival["age"]
#print(age.loc[10:20])
age_is_null = pandas.isnull(age)
print(age_is_null)
age_null_true = age[age_is_null]
age_null_count = len(age_null_true)

print(age_null_count)
