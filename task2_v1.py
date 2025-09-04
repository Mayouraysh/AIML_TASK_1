import pandas as pd
df = pd.read_csv("record.csv")
print("Head: ")
print(df.head())
print("Info: ")
print(df.info())
print("Describe: ")
print(df.describe())


