#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 12:08:13 2023

@author: sonyanedbaylo
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load your modified DataFrame with features (X) and target variable (y)
df = pd.read_excel('CleanNewDiabetes_with_BMI_range.xlsx')

# Define X (features) and y (target variable)
X = df[['BMI 18.2-24.9', 'BMI 25.0-29.9', 'BMI 30.0-67.1']]
y = df['Outcome']  # Assuming 'Outcome' is your target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define a range of values for the number of neighbors (K)
neighbors = list(range(1, 31))  # Adjust the range as needed

# Initialize an empty list to store accuracy scores
accuracy_scores = []

# Calculate accuracy for different numbers of neighbors
for k in neighbors:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    accuracy = knn.score(X_test, y_test)
    accuracy_scores.append(accuracy)

# Create a line chart to visualize accuracy vs. number of neighbors
plt.figure(figsize=(10, 6))
plt.plot(neighbors, accuracy_scores, marker='o', linestyle='-')
plt.xlabel('Number of Neighbors (K)')
plt.ylabel('Accuracy Index')
plt.title('Accuracy vs. Number of Neighbors (K) for KNN Classifier')
plt.grid(True)
plt.xticks(neighbors)
plt.show()
