import pandas as pd

df = pd.read_csv("data/SampleSuperStore_Clean.csv")

print("Duplicates:", df.duplicated().sum())
print("Missing Values:")
print(df.isnull().sum())

print("Negative Sales:", (df["Sales"] < 0).sum())
print("Negative Quantity:", (df["Quantity"] < 0).sum())
print("Negative Discount:", (df["Discount"] < 0).sum())
print(df.shape)