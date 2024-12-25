import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Salary dataset
data = pd.read_csv("Salary_Dataset_with_Extra_Features.csv")  # Make sure the filename matches
print(data.info())  # Display dataset info
print(data.head())  # Display the first 5 rows of the dataset

# Visualization: Barplot of some data
plt.figure(figsize=(10, 6))
sns.barplot(x="Job Title", y="Salary", data=data.head(10))  # Adjust based on your dataset columns
plt.title("Top 10 Job Titles by Salary")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig("salary_visualization.png")
plt.show()

# Scatter Plot: Visualizing Salary vs. Rating
plt.figure(figsize=(10, 6))
sns.scatterplot(x="Rating", y="Salary", data=data, hue="Job Title", alpha=0.7)

# Customizing the scatter plot
plt.title("Scatter Plot of Salary vs Rating")
plt.xlabel("Company Rating")
plt.ylabel("Salary")
plt.legend(title="Job Title", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Save the scatter plot
plt.savefig("scatter_salary_vs_rating.png")
plt.show()

# -------------------------------------------------
# Advanced Visualizations for Superstore Dataset
# -------------------------------------------------

# Load the dataset
superstore_data = pd.read_csv("superstore.csv")

# Print column names to verify the structure (debugging step)
print("Columns in the dataset:", superstore_data.columns)

# Clean column names to remove any extra whitespace
superstore_data.columns = superstore_data.columns.str.strip()

# Parse the "Order.Date" column as datetime
if "Order.Date" in superstore_data.columns:
    superstore_data["Order.Date"] = pd.to_datetime(superstore_data["Order.Date"])
else:
    raise KeyError("The column 'Order.Date' is missing from the dataset.")

# Display basic information about the superstore dataset
print(superstore_data.info())
print(superstore_data.head())

# -------------------------------------------------
# Line Plot: Sales Trends Over Time by Region
# -------------------------------------------------

# Aggregate sales by Order.Date and Region
sales_trends = superstore_data.groupby(["Order.Date", "Region"])["Sales"].sum().reset_index()

# Create the line plot
plt.figure(figsize=(12, 6))
sns.lineplot(data=sales_trends, x="Order.Date", y="Sales", hue="Region", marker="o")

# Customize the plot
plt.title("Sales Trends Over Time by Region")
plt.xlabel("Order Date")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.legend(title="Region", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()

# Save the line plot
plt.savefig("lineplot_sales_trends.png")
plt.show()

# -------------------------------------------------
# Heatmap: Correlation Matrix of Sales, Profit, and Discount
# -------------------------------------------------

# Create a correlation matrix
plt.figure(figsize=(10, 8))
correlation_matrix = superstore_data[["Sales", "Profit", "Discount"]].corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")

# Customize the heatmap
plt.title("Correlation Heatmap")
plt.tight_layout()

# Save the heatmap
plt.savefig("heatmap_correlation.png")
plt.show()