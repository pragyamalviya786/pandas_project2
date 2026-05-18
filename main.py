import pandas as pd

# =========================
# LOAD DATASET
# =========================
df = pd.read_csv("sales2018.csv")

# =========================
# DATA INSPECTION
# =========================
print("First 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

# =========================
# DATA CLEANING
# =========================

# Remove unnecessary columns
columns_to_drop = ["promo_bin_2", "promo_discount_2", "promo_type_2"]

df.drop(columns=columns_to_drop, inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# =========================
# SAVE CLEANED DATASET
# =========================
df.to_csv("sales2018_cleaned.csv", index=False)

print("\nDataset cleaned successfully!")
print("Cleaned dataset saved as sales2018_cleaned.csv")

df["promo_bin_1"] = df["promo_bin_1"].fillna(0)
