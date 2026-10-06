import pandas as pd
import random

df = pd.read_csv("data/SampleSuperStore.csv")

# Add duplicate rows
duplicates = df.head(5)

dirty_csv = pd.concat([df, duplicates], ignore_index=True)

# Add missing values
for col in ["Sales", "Profit", "Category"]:
    random_rows = random.sample(range(len(dirty_csv)), 10)
    dirty_csv.loc[random_rows, col] = None

# Add negative values
for col in ["Sales", "Discount", "Quantity"]:
    negative_rows = random.sample(range(len(dirty_csv)), 5)
    dirty_csv.loc[negative_rows, col] = -54

# Save dirty dataset
dirty_csv.to_csv("data/SampleSuperStore_Dirty.csv", index=False)

