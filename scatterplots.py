import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("diabetesinfo_cleanednew.csv")

# Remove the "Outcome" column for scatterplot matrix
features = data.drop(columns=["Outcome"])

# Create a scatterplot matrix for Age vs other features
sns.set(style="ticks")
sns.pairplot(data, hue="Outcome", vars=features, diag_kind='hist', palette="Set1", x_vars=["Age"])

plt.suptitle("Scatterplot Matrix (Age vs Other Features)")
plt.show()

