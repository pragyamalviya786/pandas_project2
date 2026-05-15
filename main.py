import pandas as pd

df = pd.read_csv("sales2018.csv")

# inspect dataset
print(df.head())
print(df.info())
print(df.shape)
print(df.isnull().sum())

# cleaning
df.drop(columns=["promo_bin_2", "promo_discount_2", "promo_type_2"], inplace=True)

# save cleaned file
df.to_csv("sales2018_cleaned.csv", index=False)

print("Dataset cleaned successfully")
