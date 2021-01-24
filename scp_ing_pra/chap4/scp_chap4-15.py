import pandas as pd

df = pd.read_csv("firehydrant.csv", encoding="shift-jis")

print(len(df))
print(df.columns.values)
