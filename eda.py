import pandas as pd

df = pd.read_csv("customer_reviews.csv")
print("Dataset Shape:")
print("Shape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nAverage Rating:")
print(df["Rating"].mean())

print("\nCategory Wise Ratings:")
print(df.groupby("Category")["Rating"].mean())