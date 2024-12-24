import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
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


