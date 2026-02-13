mport pandas as pd

df = pd.read_csv("data.csv")

print("FIRST 5 ROWS")
print(df.head())

print("\nINFO")
print(df.info())

print("\nDESCRIPTION")
print(df.describe())

print("\nMISSING VALUES")
print(df.isnull().sum())

df.fillna(0, inplace=True)

filtered_data = df[df["Age"] > 15]
print("\nFILTERED DATA (Age > 15)")
print(filtered_data)

sorted_data = df.sort_values(by="Marks", ascending=False)
print("\nSORTED DATA (Marks DESC)")
print(sorted_data)

grouped_data = df.groupby("Grade")["Marks"].mean()
print("\nAVERAGE MARKS BY GRADE")
print(grouped_data)

df["Bonus_Marks"] = df["Marks"] * 0.10

df.to_csv("cleaned_data.csv", index=False)

print("\nDONE ✅ cleaned_data.csv created")
