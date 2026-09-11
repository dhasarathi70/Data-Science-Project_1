#Unit 3 Project - Movie Rating Analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
df = pd.read_excel("Movie rating analysis.xlsx")

# Display dataset
print("MOVIE RATING DATASET")
print(df)

# First 5 Rows
print("\nFIRST 5 ROWS")
print(df.head())

# First 3 Rows
print("\nFIRST 3 ROWS")
print(df.head(3))

# Last 5 Rows
print("\nLAST 5 ROWS")
print(df.tail())

# Last 3 Rows
print("\nLAST 3 ROWS")
print(df.tail(3))

# Information
print("\nDATASET INFORMATION")
print(df.info())

# Data Types
print("\nDATA TYPES")
print(df.dtypes)

# Number of Rows and Columns
print("\nSIZE OF DATASET")
print(df.shape)

# Average Rating
print("\nAVERAGE RATING")
average = df[["Story Rating", "Direction Rating", "Acting Rating", "Overall Rating"]].mean()
print(average)

# Minimum Rating
print("\nMINIMUM RATING")
mini = df[["Story Rating", "Direction Rating", "Acting Rating", "Overall Rating"]].min()
print(mini)

# Maximum Rating
print("\nMAXIMUM RATING")
maxi = df[["Story Rating", "Direction Rating", "Acting Rating", "Overall Rating"]].max()
print(maxi)

print("\nHISTOGRAM")

sns.histplot(data=df, x="Overall Rating", bins=5)

plt.title("Distribution of Overall Movie Ratings")
plt.xlabel("Overall Rating")
plt.ylabel("Number of Movies")
plt.show()


print("\nBOX PLOT")

sns.boxplot(data=df[
    ["Story Rating", "Direction Rating", "Acting Rating", "Overall Rating"]
])

plt.title("Comparison of Movie Ratings")
plt.xlabel("Rating Categories")
plt.ylabel("Rating")
plt.show()


print("\nSTORY RATING VS DIRECTION RATING")

sns.scatterplot(
    data=df,
    x="Story Rating",
    y="Direction Rating"
)

plt.title("Story Rating vs Direction Rating")
plt.xlabel("Story Rating")
plt.ylabel("Direction Rating")
plt.show()

print("\nCORRELATION")

corr = df[
    ["Story Rating", "Direction Rating", "Acting Rating", "Overall Rating"]
].corr()

print(corr)

sns.heatmap(corr, annot=True)

plt.title("Movie Rating Correlation Heatmap")
plt.show()


print("\nHIGHEST RATED MOVIE")

highest = df.loc[df["Overall Rating"].idxmax()]

print(highest)


print("\nLOWEST RATED MOVIE")

lowest = df.loc[df["Overall Rating"].idxmin()]

print(lowest)


print("\nAVERAGE OF EACH RATING CATEGORY")

category_average = df[
    ["Story Rating", "Direction Rating", "Acting Rating", "Overall Rating"]
].mean()

print(category_average)