import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.metrics import accuracy_score

# Load the data
data = pd.read_csv("diabetesinfo_cleanednew.csv")

# Specify columns to exclude from features
exclude_columns = ['Age', 'SkinThickness']  # Add column names to exclude here

# Create a list of columns to use as features (excluding the 'Outcome' column and any specified columns to exclude)
features = [col for col in data.columns if col != 'Outcome' and col not in exclude_columns]

# Split the data into features and target
X = data[features]
y = data["Outcome"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# KNN Classification
k_values = list(range(1, 21))
knn_accuracies = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    knn_accuracies.append(accuracy)

# Naive Bayes Classification
nb_methods = [GaussianNB(), MultinomialNB(), BernoulliNB()]
nb_method_names = ["GaussianNB", "MultinomialNB", "BernoulliNB"]
nb_accuracies = []

for nb, method_name in zip(nb_methods, nb_method_names):
    nb.fit(X_train, y_train)
    y_pred = nb.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    nb_accuracies.append(accuracy)

# Create line graph for KNN
plt.figure(figsize=(10, 5))
plt.plot(k_values, knn_accuracies, marker='o', linestyle='-', color='blue')
plt.title("KNN Accuracy vs. Number of Neighbors")
plt.xlabel("Number of Neighbors (k)")
plt.ylabel("Accuracy")
plt.grid(True)
plt.show()

# Create bar chart for Naive Bayes methods
plt.figure(figsize=(10, 5))
sns.barplot(x=nb_method_names, y=nb_accuracies, palette="viridis")
plt.title("Naive Bayes Accuracy for Different Methods")
plt.xlabel("NB Method")
plt.ylabel("Accuracy")
plt.ylim(0, 1)
plt.xticks(rotation=45)
plt.show()
