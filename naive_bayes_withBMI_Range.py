#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 15:14:29 2023

@author: sonyanedbaylo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.metrics import accuracy_score, classification_report

# Assuming your dataset is loaded into a DataFrame named 'df'
# Replace the following line with your own dataset loading if needed
df = pd.read_excel('CleanNewDiabetes_with_BMI_range.xlsx')



# Excluding 'Pregnancies' from the list of features
features = ['Glucose', 'BloodPressure', 'Insulin', 'DiabetesPedigreeFunction', 'Pregnancies', 'BMI 18.2-24.9',
'BMI 25.0-29.9', 'BMI 30.0-67.1']

# Split the dataset into features (X) and target (y)
X = df[features]
y = df['Outcome']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize lists to store accuracy values for different Naive Bayes methods
methods = ['Gaussian', 'Multinomial', 'Bernoulli']
accuracy_scores = []

# Loop through different Naive Bayes methods
for method in methods:
    if method == 'Gaussian':
        nb = GaussianNB()
    elif method == 'Multinomial':
        nb = MultinomialNB()
    elif method == 'Bernoulli':
        nb = BernoulliNB()
    nb.fit(X_train, y_train)
    y_pred_nb = nb.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred_nb)
    accuracy_scores.append(accuracy)

# Create a bar graph to visualize accuracy for different Naive Bayes methods
plt.figure(figsize=(10, 6))
plt.bar(methods, accuracy_scores, color=['blue', 'green', 'red'])
plt.title('Accuracy for Different Naive Bayes Methods')
plt.xlabel('Naive Bayes Method')
plt.ylabel('Accuracy')
plt.ylim(0, 1.0)
plt.grid(axis='y')
plt.show()

# Identify the best Naive Bayes method
best_method = methods[np.argmax(accuracy_scores)]
print(f"The best Naive Bayes method is {best_method} with accuracy {max(accuracy_scores):.2f}")

# Train the Naive Bayes classifier with the best method
if best_method == 'Gaussian':
    best_nb = GaussianNB()
elif best_method == 'Multinomial':
    best_nb = MultinomialNB()
else:
    best_nb = BernoulliNB()
best_nb.fit(X_train, y_train)
y_pred_best_nb = best_nb.predict(X_test)

# Evaluate the best Naive Bayes model
best_accuracy_nb = accuracy_score(y_test, y_pred_best_nb)
print(f"\nBest Naive Bayes Classifier ({best_method}):")
print(f"Accuracy: {best_accuracy_nb:.2f}")
print(classification_report(y_test, y_pred_best_nb))


