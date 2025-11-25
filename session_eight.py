import pandas as np 


testdf = np.read_csv('data.csv')
# print(testdf.info())
# print(testdf.to_string())
# print(testdf.head())
# print(testdf.tail())
# print(testdf.isnull().sum())

# mean = testdf["Calories"].mean()
# testdf["Calories"].fillna(mean, inplace=True)
# print(testdf.to_string())

# median = testdf["Calories"].median()
# testdf.fillna({"Calories":median}, inplace=True)
# print(testdf.to_string())

# print(testdf.corr())
# print(testdf.describe())
# print(testdf["Duration"].value_counts())
# print(testdf["Duration"].unique())
# chgcolname = testdf.rename(columns={"Calories":"Cal"})
# print(chgcolname)

# newdf = testdf[testdf["Calories"]>290]
# print(newdf)

# groupeddf = testdf.groupby("Duration")["Calories"].agg('min','max')
# print(groupeddf)

###############################################