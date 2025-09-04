import pandas as pd

df = pd.read_csv("nullrecord.csv")
print("og data:")
print(df)

print("missing values in each column:")
print(df.isnull().sum())

df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Runs'] = df['Runs'].fillna(df['Runs'].mean())

print("data clenad:")
print(df)

df.to_csv("nullrecord_clean.csv", index=False)
print("cleaned file saved as nullrecord_clean.csv")
