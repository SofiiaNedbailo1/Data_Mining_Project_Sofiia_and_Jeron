import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("diabetesinfo_cleanednew.csv")

# Define the pairs of variables for scatter diagrams
scatter_pairs = [("Age", "Pregnancies"), ("Glucose", "Insulin"), ("SkinThickness", "BMI")]

# Create scatter diagrams
plt.figure(figsize=(15, 5))

for i, (x_var, y_var) in enumerate(scatter_pairs, 1):
    plt.subplot(1, 3, i)
    plt.scatter(data[x_var], data[y_var], alpha=0.5)
    plt.title(f"{x_var} vs {y_var}")
    plt.xlabel(x_var)
    plt.ylabel(y_var)

plt.tight_layout()
plt.show()
