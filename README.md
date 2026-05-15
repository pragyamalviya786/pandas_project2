# 🛒 Retail Sales Data Cleaning using Pandas

## 📌 Project Overview
This project demonstrates a complete data cleaning workflow using **Python** and **Pandas** on a retail sales dataset.  
The objective is to preprocess raw sales data by removing unnecessary columns and preparing the dataset for further analysis, reporting, and visualization.

---

## 👩‍💻 Author
### **Pragya Malviya**

---

## 🛠️ Tech Stack
- 🐍 Python
- 📊 Pandas

---

## 📂 Dataset Information

### 📥 Input File
`sales2018.csv`

### 📤 Cleaned Output File
`sales2018_cleaned.csv`

---

## ✨ Key Operations Performed
✔️ Loaded the dataset using Pandas  
✔️ Inspected dataset structure and dimensions  
✔️ Checked missing values  
✔️ Removed unnecessary promotional columns  
✔️ Exported cleaned dataset into a new CSV file  

---

## 🗑️ Columns Removed
The following columns were removed from the dataset:

- `promo_bin_2`
- `promo_discount_2`
- `promo_type_2`

---

## 💻 Python Implementation

```python
import pandas as pd

# Load dataset
df = pd.read_csv("sales2018.csv")

# Inspect dataset
print(df.head())
print(df.info())
print(df.shape)
print(df.isnull().sum())

# Data cleaning
df.drop(columns=[
    "promo_bin_2",
    "promo_discount_2",
    "promo_type_2"
], inplace=True)

# Save cleaned dataset
df.to_csv("sales2018_cleaned.csv", index=False)

print("Dataset cleaned successfully")
