import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("customer_reviews.csv")

category_ratings = df.groupby("Category")["Rating"].mean()

category_ratings.plot(kind="bar")

plt.title("Average Rating by Category")
plt.xlabel("Category")
plt.ylabel("Average Rating")

plt.show()