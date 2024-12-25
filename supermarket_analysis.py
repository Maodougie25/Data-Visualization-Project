import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------------------------
# Supermarket Sales Dataset Analysis
# -------------------------------------------------

# Load the dataset
data = pd.read_csv("supermarket_sales.csv")

# Display basic dataset information
print("Dataset Information:")
print(data.info())
print("\nFirst Few Rows of Data:")
print(data.head())

# -------------------------------------------------
# Bar Plot: Total Sales by City
# -------------------------------------------------

# Aggregate total sales by city
city_sales = data.groupby("City")["Total"].sum().reset_index()

# Create a bar plot
plt.figure(figsize=(8, 6))
sns.barplot(data=city_sales, x="City", y="Total", palette="viridis")

# Customize the plot
plt.title("Total Sales by City")
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.tight_layout()

# Save the plot
plt.savefig("barplot_city_sales.png")
plt.show()

# -------------------------------------------------
# Line Plot: Daily Sales Trends
# -------------------------------------------------

# Convert the "Date" column to datetime
data["Date"] = pd.to_datetime(data["Date"])

# Aggregate daily sales
daily_sales = data.groupby("Date")["Total"].sum().reset_index()

# Create a line plot
plt.figure(figsize=(12, 6))
sns.lineplot(data=daily_sales, x="Date", y="Total", marker="o")

# Customize the plot
plt.title("Daily Sales Trends")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig("lineplot_daily_sales.png")
plt.show()

# -------------------------------------------------
# Heatmap: Correlation Matrix
# -------------------------------------------------

# Select numeric columns for correlation analysis
numeric_data = data[["Unit price", "Quantity", "Total", "cogs", "gross income", "Rating"]]

# Calculate the correlation matrix
correlation_matrix = numeric_data.corr()

# Create a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")

# Customize the heatmap
plt.title("Correlation Heatmap")
plt.tight_layout()

# Save the heatmap
plt.savefig("heatmap_correlation.png")
plt.show()