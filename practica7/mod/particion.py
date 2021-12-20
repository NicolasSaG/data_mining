import pandas as pd


file = pd.read_csv("tabla_hechos.csv",  encoding="utf-8")
df = pd.DataFrame(file)
print(df.head(30))
