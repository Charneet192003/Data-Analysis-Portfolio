import pandas as pd


df = pd.read_csv('marks.csv')
print(df)


print("First five rows of the dataset:")
print(df.head())


print("\nSummary statistics:")
print(df.describe())


print("\nMissing values in each column:")
print(df.isnull().sum())


print("\nData types of each column:")
print(df.dtypes)




