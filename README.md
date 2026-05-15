# Sales Data Cleaning Project

## Overview
This project focuses on cleaning a retail sales dataset using Python and Pandas.  
The script removes unnecessary columns and prepares the dataset for further analysis and visualization.

---

## Technologies Used
- Python
- Pandas

---

## Dataset Files

### Input
`sales2018.csv`

### Output
`sales2018_cleaned.csv`

---

## Features
- Load CSV dataset
- Inspect dataset structure
- Check null values
- Remove unnecessary columns
- Save cleaned dataset

---

## Columns Removed
The following columns were removed from the dataset:

- `promo_bin_2`
- `promo_discount_2`
- `promo_type_2`

---

## Python Script

```python
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
