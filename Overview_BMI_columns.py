#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 14:49:01 2023

@author: sonyanedbaylo
"""

#The overview of eachBMI category per percentage

import pandas as pd
import matplotlib.pyplot as plt

# Load your modified DataFrame with BMI columns
df = pd.read_excel('CleanNewDiabetes_with_BMI_range.xlsx')

# Calculate the percentage of each BMI group
total_count = len(df)
percentage_18_24 = (df['BMI 18.2-24.9'] > 0).sum() / total_count * 100
percentage_25_29 = (df['BMI 25.0-29.9'] > 0).sum() / total_count * 100
percentage_30_67 = (df['BMI 30.0-67.1'] > 0).sum() / total_count * 100

# Create a bar chart showing the percentages
plt.figure(figsize=(8, 6))
plt.bar(['BMI 18.2-24.9', 'BMI 25.0-29.9', 'BMI 30.0-67.1'], [percentage_18_24, percentage_25_29, percentage_30_67])
plt.xlabel('BMI Group')
plt.ylabel('Percentage (%)')
plt.title('Percentage of Each BMI Group in the Dataset')
plt.ylim(0, 100)

# Annotate the bars with their respective percentages
for i, percentage in enumerate([percentage_18_24, percentage_25_29, percentage_30_67]):
    plt.text(i, percentage + 2, f'{percentage:.2f}%', ha='center', va='bottom')

# Save the bar chart as a PNG image
plt.savefig('percentage_bmi_groups.png')

# Show the chart (optional)
plt.show()



##Try sctter without 0 values ,the following code represents the scatterplots for the BMI ranges columns (Glucose Scetterplot)

import pandas as pd
import matplotlib.pyplot as plt

# Load your modified DataFrame with BMI columns and glucose
df = pd.read_excel('CleanNewDiabetes_with_BMI_range.xlsx')

# Replace 0 values in BMI columns with NaN
df['BMI 18.2-24.9'].replace(0, float('nan'), inplace=True)
df['BMI 25.0-29.9'].replace(0, float('nan'), inplace=True)
df['BMI 30.0-67.1'].replace(0, float('nan'), inplace=True)

# Create separate scatter plots for each BMI range column with glucose
plt.figure(figsize=(12, 4))

# Scatter plot for BMI 18.2-24.9 vs. Glucose
plt.subplot(131)
plt.scatter(df['BMI 18.2-24.9'], df['Glucose'])
plt.xlabel('BMI 18.2-24.9')
plt.ylabel('Glucose')
plt.title('Scatter Plot: BMI 18.2-24.9 vs. Glucose')

# Scatter plot for BMI 25.0-29.9 vs. Glucose
plt.subplot(132)
plt.scatter(df['BMI 25.0-29.9'], df['Glucose'])
plt.xlabel('BMI 25.0-29.9')
plt.ylabel('Glucose')
plt.title('Scatter Plot: BMI 25.0-29.9 vs. Glucose')

# Scatter plot for BMI 30.0-67.1 vs. Glucose
plt.subplot(133)
plt.scatter(df['BMI 30.0-67.1'], df['Glucose'])
plt.xlabel('BMI 30.0-67.1')
plt.ylabel('Glucose')
plt.title('Scatter Plot: BMI 30.0-67.1 vs. Glucose')

# Adjust spacing between subplots
plt.tight_layout()

# Show the plots
plt.show()

#Below the scatterplots for each variable will be created in 1 png

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your modified DataFrame with BMI columns and other variables
df = pd.read_excel('CleanNewDiabetes_with_BMI_range.xlsx')

# Replace 0 values in BMI columns with NaN
df['BMI 18.2-24.9'].replace(0, float('nan'), inplace=True)
df['BMI 25.0-29.9'].replace(0, float('nan'), inplace=True)
df['BMI 30.0-67.1'].replace(0, float('nan'), inplace=True)

# Get a list of all column names except 'Glucose' and 'BMI' columns
variables_to_plot = [col for col in df.columns if col not in ['Glucose', 'BMI 18.2-24.9', 'BMI 25.0-29.9', 'BMI 30.0-67.1']]

# Create a grid of scatter plots
num_bmi_columns = 3
num_variables = len(variables_to_plot)
fig, axes = plt.subplots(num_variables, num_bmi_columns, figsize=(12, 8))

for i, bmi_column in enumerate(['BMI 18.2-24.9', 'BMI 25.0-29.9', 'BMI 30.0-67.1']):
    for j, variable in enumerate(variables_to_plot):
        ax = axes[j, i]
        sns.scatterplot(data=df, x=bmi_column, y=variable, ax=ax, alpha=0.5)
        ax.set_xlabel(bmi_column)
        ax.set_ylabel(variable)
        ax.set_title(f'{bmi_column} vs. {variable}')

# Adjust spacing between subplots and save as a PNG
plt.tight_layout()
plt.savefig('scatterplot_grid.png')
plt.show()

#Below the scatterplots for each variable will be created in 2 pngs

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your modified DataFrame with BMI columns and other variables
df = pd.read_excel('CleanNewDiabetes_with_BMI_range.xlsx')

# Replace 0 values in BMI columns with NaN
df['BMI 18.2-24.9'].replace(0, float('nan'), inplace=True)
df['BMI 25.0-29.9'].replace(0, float('nan'), inplace=True)
df['BMI 30.0-67.1'].replace(0, float('nan'), inplace=True)

# Get a list of all column names except 'Glucose' and 'BMI' columns
variables_to_plot = [col for col in df.columns if col not in ['Glucose', 'BMI 18.2-24.9', 'BMI 25.0-29.9', 'BMI 30.0-67.1']]

# Split the variables into two parts
variables_part1 = variables_to_plot[:len(variables_to_plot) // 2]
variables_part2 = variables_to_plot[len(variables_to_plot) // 2:]

# Create a function to create a scatterplot grid
def create_scatterplot_grid(bmi_columns, variables, filename):
    num_bmi_columns = len(bmi_columns)
    num_variables = len(variables)
    fig, axes = plt.subplots(num_variables, num_bmi_columns, figsize=(12, 8), squeeze=False)

    for i, bmi_column in enumerate(bmi_columns):
        for j, variable in enumerate(variables):
            ax = axes[j, i]
            sns.scatterplot(data=df, x=bmi_column, y=variable, ax=ax, alpha=0.5)
            ax.set_xlabel(bmi_column)
            ax.set_ylabel(variable)
            ax.set_title(f'{bmi_column} vs. {variable}')

    # Adjust spacing between subplots and save as a PNG
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()

# Create scatterplot grid for all three BMI columns (Part 1 variables)
create_scatterplot_grid(['BMI 18.2-24.9', 'BMI 25.0-29.9', 'BMI 30.0-67.1'], variables_part1, 'scatterplot_part1.png')

# Create scatterplot grid for all three BMI columns (Part 2 variables)
create_scatterplot_grid(['BMI 18.2-24.9', 'BMI 25.0-29.9', 'BMI 30.0-67.1'], variables_part2, 'scatterplot_part2.png')

##Below the heatmap for the variables with most correlation with BMI will be created, to see even bigger pattern

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your modified DataFrame with BMI columns and other variables
df = pd.read_excel('CleanNewDiabetes_with_BMI_range.xlsx')

# Replace 0 values in BMI columns with NaN
df['BMI 18.2-24.9'].replace(0, float('nan'), inplace=True)
df['BMI 25.0-29.9'].replace(0, float('nan'), inplace=True)
df['BMI 30.0-67.1'].replace(0, float('nan'), inplace=True)

# Select columns for the correlation heatmap
columns_to_correlate = ['BMI 18.2-24.9', 'BMI 25.0-29.9', 'BMI 30.0-67.1', 'Insulin', 'Outcome', 'SkinThickness']
correlation_matrix = df[columns_to_correlate].corr()

# Create a correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()


