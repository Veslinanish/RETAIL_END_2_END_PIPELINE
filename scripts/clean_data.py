import pandas as pd

# =====================================
# LOAD DIRTY DATASET
# =====================================

df = pd.read_csv("data/SampleSuperStore_Dirty.csv")

print("Before Cleaning")
print("Rows:", len(df))

# =====================================
# 1. REMOVE DUPLICATES
# =====================================

duplicates_before = df.duplicated().sum()

df = df.drop_duplicates()

print("\nDuplicates Removed:", duplicates_before)

# =====================================
# 2. HANDLE MISSING VALUES
# =====================================

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Fill missing Category with Unknown
df["Category"] = df["Category"].fillna("Unknown")

# Fill missing Sales with median
df["Sales"] = df["Sales"].fillna(df["Sales"].median())

# Fill missing Profit with median
df["Profit"] = df["Profit"].fillna(df["Profit"].median())

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# =====================================
# 3. REMOVE NEGATIVE SALES
# =====================================

negative_sales = (df["Sales"] < 0).sum()

df = df[df["Sales"] >= 0]

print("\nNegative Sales Removed:", negative_sales)

# =====================================
# 4. REMOVE NEGATIVE QUANTITY
# =====================================

negative_quantity = (df["Quantity"] < 0).sum()

df = df[df["Quantity"] >= 0]

print("Negative Quantity Removed:", negative_quantity)

# =====================================
# 5. REMOVE INVALID DISCOUNT
# =====================================

invalid_discount = (
    (df["Discount"] < 0) |
    (df["Discount"] > 1)
).sum()

df = df[
    (df["Discount"] >= 0) &
    (df["Discount"] <= 1)
]

print("Invalid Discount Removed:", invalid_discount)

# =====================================
# 6. FIX CATEGORY TYPO
# =====================================

df["Category"] = df["Category"].replace(
    "Furnture",
    "Furniture"
)

# =====================================
# 7. REMOVE EXTRA SPACES
# =====================================

df["Region"] = df["Region"].str.strip()

# =====================================
# SAVE CLEAN DATASET
# =====================================

df.to_csv(
    "data/SampleSuperStore_Clean.csv",
    index=False
)

print("\nAfter Cleaning")
print("Rows:", len(df))

print("\nClean Dataset Saved Successfully!")