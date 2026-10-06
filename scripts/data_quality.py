import pandas as pd
df=pd.read_csv("data/sampleSuperStore_Dirty.csv")

#checking the shape
print("SHAPE")
print(df.shape)

#checking the information
print("INFO")
print(df.info())
print(" ")

#checking null values
print("NULL VALUES")
print(df.isnull().sum())
print(" ")

#checking duplicated values
print("DUPLICATED VALUES")
print(df.duplicated().sum())
print(" ")

#checking negative values for sales
print("NEGATIVE VALUES OF SALES")
print((df["Sales"]<0).sum())
print(" ")

#checking negative values for profit
print("NEGATIVE VALUES OF QUANTITY")
print((df["Quantity"]<0).sum())
print(" ")

#checking negative values for discount
print("NEGATIVE VALUES OF DISCOUNT")
print((df["Discount"]<0).sum())
