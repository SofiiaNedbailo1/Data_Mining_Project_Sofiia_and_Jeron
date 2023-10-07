import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv("diabetesinfo_cleanednew.csv")

# Create boxplots for each feature compared to "Outcome"
features = data.columns[:-1]  # Exclude the "Outcome" column

plt.figure(figsize=(16, 10))
for i, feature in enumerate(features, 1):
    plt.subplot(3, 3, i)  # Create a 3x3 grid of subplots
    sns.boxplot(x="Outcome", y=feature, data=data, palette="Set1")
    plt.title(f"{feature} vs Outcome")
    plt.xlabel("Outcome")
    plt.ylabel(feature)

plt.tight_layout()
plt.show()
