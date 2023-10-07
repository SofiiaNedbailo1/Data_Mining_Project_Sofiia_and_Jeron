import pandas as pd

# Load the data
data = pd.read_csv("diabetesinfo_cleanednew.csv")

# Calculate the correlation matrix
correlation_matrix = data.corr()

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()
