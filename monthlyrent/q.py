import pandas as pd
df = pd.read_csv("House_Rent_Dataset.csv")
for col in df.columns:
    print(f"\nColumn: {col}")
    print(df[col].unique())
