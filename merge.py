import pandas as pd

a = pd.read_csv("generated_data.csv")
b = pd.read_csv("manual_data.csv")
b = b.dropna(axis=1)
merged = a.merge(b, on='stage_name')
merged.to_csv("stage_data.csv", index=False)