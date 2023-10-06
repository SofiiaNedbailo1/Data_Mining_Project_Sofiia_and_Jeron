#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 13:18:26 2023

@author: sonyanedbaylo
"""




import pandas as pd

# Load your original Excel file
df = pd.read_csv('diabetesinfo_cleanednew.csv')
# Create three new columns initialized with zeros
df['BMI 18.2-24.9'] = 0
df['BMI 25.0-29.9'] = 0
df['BMI 30.0-67.1'] = 0

# Assign values to the new columns based on the BMI ranges
df.loc[(df['BMI'] >= 18.2) & (df['BMI'] <= 24.9), 'BMI 18.2-24.9'] = df['BMI']
df.loc[(df['BMI'] >= 25.0) & (df['BMI'] <= 29.9), 'BMI 25.0-29.9'] = df['BMI']
df.loc[df['BMI'] >= 30.0, 'BMI 30.0-67.1'] = df['BMI']

# Drop the original BMI column
df = df.drop(columns=['BMI'])

# Save the modified DataFrame to a new Excel file
df.to_excel('CleanNewDiabetes_with_BMI_range.xlsx', index=False)

