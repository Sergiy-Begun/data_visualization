#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 17:39:55 2024

@author: sergiybegun
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# useful links to refresh knowledge
# seaborn API reference https://seaborn.pydata.org/api.html
# Matplotlib API Reference https://matplotlib.org/stable/api/index.html

# Fifa Data Set. Linear Chart Graph

# Path to the data
data_filepath = "input_data/fifa.csv"

# Read the data from file parsing the date of events as a date column, and making the Date column as an index column
data_for_investigation = pd.read_csv(data_filepath, index_col="Date", parse_dates=True)


# Set the width and height of the figure
plt.figure(figsize=(16,6))

# Setting the title for the chart
plt.title("Historical FIFA rankings for six countries")

# Add label for horizontal axis
plt.xlabel("Date")

# Add label for vertical axis
plt.ylabel("Rank")

# Line chart showing how data_for_investigation evolved over time 
sns.lineplot(data=data_for_investigation)

plt.show()

#__________________________________________________________________________________________

# Museum Visitors Data Set. Linear Chart Graph.

# file path to the data
museum_filepath = "input_data/museum_visitors.csv"

# reading the data from file
museum_data = pd.read_csv(museum_filepath, index_col="Date", parse_dates=True)

# Number of visitors to the Chinese American Museum in July 2018
ca_museum_jul18 = museum_data.at["2018-07-01", "Chinese American Museum"]

print("The number of visitors to the Chinese American Museum in July 2018 (ca_museum_jul18) = ", ca_museum_jul18)

# In October 2018, how many more visitors did Avila Adobe receive than the Firehouse Museum?
avila_oct18_difference = museum_data.at["2018-10-01", "Avila Adobe"] - museum_data.at["2018-10-01", "Firehouse Museum"]

print("In October 2018, Avila Adobe received ", avila_oct18_difference, " more visitors than the Firehouse Museum")

# Set the width and height of the figure
plt.figure(figsize=(16,6))

# Setting the title for the chart
plt.title("The number of visitors to each museum over time")

# Add label for horizontal axis
plt.xlabel("Date")

# Add label for vertical axis
plt.ylabel("The number of visitors per month")

# Line chart showing how museum_data evolved over time 
sns.lineplot(data=museum_data)

plt.show()

#__________________________________________________________________________________________

# Flights Data Set. BarPlot & HeatMap Graphs.

# ================ BarPlot =============================

# Path of the file to read
flight_filepath = "input_data/flight_delays.csv"

# Read the file into a variable flight_data, and setting Month column as an index
flight_data = pd.read_csv(flight_filepath, index_col="Month")

# Set the width and height of the figure
plt.figure(figsize=(10,6))

# Add title
plt.title("Average Arrival Delay for Spirit Airlines Flights, by Month")

# Bar chart showing average arrival delay for Spirit Airlines flights by month
sns.barplot(x=flight_data.index, y=flight_data['NK'])

# Add label for vertical axis
plt.ylabel("Arrival delay (in minutes)")

# ================ HeatMap =============================

# Set the width and height of the figure
plt.figure(figsize=(14,7))

# Add title
plt.title("Average Arrival Delay for Each Airline, by Month")

# Add label for horizontal axis
plt.xlabel("Airline")

# Heatmap showing average arrival delay for each airline by month
sns.heatmap(data=flight_data, annot=True)

#__________________________________________________________________________________________

# IGN reviews Data Set. BarPlot & HeatMap Graphs.

# ================ BarPlot =============================

# Path of the file to read
ign_filepath = "input_data/ign_scores.csv"

# Read the file into a variable flight_data, and setting Platform column as an index
ign_data = pd.read_csv(ign_filepath, index_col="Platform")

# What is the highest average score received by PC games, for any genre?

high_score = -1.0

for col in ign_data[(ign_data.index == "PC")]:
    cur_score = ign_data.at["PC",col]
    if high_score < 0.0:
        high_score = cur_score
    if cur_score > high_score:
        high_score = cur_score

print("The highest average score received by PC games, for any genre = ", high_score)

# On the Playstation Vita platform, which genre has the 
# lowest average score? Please provide the name of the column, and put your answer 
# in single quotes (e.g., 'Action', 'Adventure', 'Fighting', etc.)

worst_genre = ""

min_score = -1.0

for col in ign_data[(ign_data.index == "PlayStation Vita")]:
    cur_score = ign_data.at["PlayStation Vita",col]
    if min_score < 0.0:
        worst_genre = col
        min_score = cur_score
    if cur_score < min_score:
        worst_genre = col
        min_score = cur_score
        
print("worst_genre for Playstation Vita = ", worst_genre)

# Bar chart showing average score for racing games by platform

# Set the width and height of the figure
plt.figure(figsize=(35,10))

# Add title
plt.title("Average score for racing games by platform")

# Bar chart showing average score for racing games by platform
sns.barplot(x=ign_data.index, y=ign_data['Racing'])

# Add label for vertical axis
plt.ylabel("Score Value")

# ================ HeatMap =============================

# Heatmap showing average game score by platform and genre

# Set the width and height of the figure
plt.figure(figsize=(14,7))

# Add title
plt.title("Average game score by platform and genre")

# Add label for horizontal axis
plt.xlabel("Platform")

# Heatmap showing average game score by platform and genre
sns.heatmap(data=ign_data, annot=True)

#__________________________________________________________________________________________

# A (synthetic) dataset of insurance charges. Scatter Plot. Color-coded scatter plots.
# Scatter plots for categorical variables

# ================ Scatter Plot =============================

# Path of the file to read
insurance_filepath = "input_data/insurance.csv"

# Read the file into a variable insurance_data
insurance_data = pd.read_csv(insurance_filepath)

# Set the width and height of the figure
plt.figure(figsize=(14,7))

# Add title
plt.title("Insurance charges dependence on body mass index (BMI)")

# simple scatter plot
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'])

# adding a regression line to that scatter plot (best fit of the data to check the dependences)
sns.regplot(x=insurance_data['bmi'], y=insurance_data['charges'])

# ================ Color-coded scatter plots =============================

# Using the same data set

# Set the width and height of the figure
plt.figure(figsize=(10,7))

# Add title
plt.title("Insurance charges dependence on body mass index (BMI)")

# use different color for data depending of smoker value ("yes" or "not", 
# could be other color if, for example, smoker value would be "unknown" or something else)
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'], hue=insurance_data['smoker'])

# adding separate regression lines for data of smokers and no-smokers using sns.lmplot
sns.lmplot(x="bmi", y="charges", hue="smoker", data=insurance_data)

# ================ Scatter plots for categorical variables =============================

# Using the same data set

# Set the width and height of the figure
plt.figure(figsize=(14,14))

# Add title
plt.title("Insurance charges dependence on smoking habits")

# using sns.swarmplot command to plot dependence of charges on smoking habits
sns.swarmplot(x=insurance_data['smoker'], y=insurance_data['charges'])

#__________________________________________________________________________________________
# Another data set on favorite candies

# Path of the file to read
candy_filepath = "input_data/candy.csv"
 
# reading the data from file
candy_data = pd.read_csv(candy_filepath,index_col="id")

# Which candy was more popular with survey respondents:
# '3 Musketeers' or 'Almond Joy'?
more_popular = ""

three_Musketeers_id = candy_data[(candy_data.competitorname == "3 Musketeers")].index[0]

Almond_Joy_id = candy_data[(candy_data.competitorname == "Almond Joy")].index[0]

if (candy_data.at[three_Musketeers_id,"winpercent"] > candy_data.at[Almond_Joy_id,"winpercent"]):
    more_popular = "3 Musketeers"
else:
    more_popular = "Almond Joy"

print("more_popular is ", more_popular)

# Which candy has higher sugar content: 'Air Heads' or 'Baby Ruth'?
more_sugar = ""

Air_Heads_id = candy_data[(candy_data.competitorname == "Air Heads")].index[0]

Baby_Ruth_id = candy_data[(candy_data.competitorname == "Baby Ruth")].index[0]

if (candy_data.at[Air_Heads_id,"sugarpercent"] > candy_data.at[Baby_Ruth_id,"sugarpercent"]):
    more_sugar = "Air Heads"
else:
    more_sugar = "Baby Ruth"

# Scatter plot showing the relationship between 'sugarpercent' and 'winpercent'

# Set the width and height of the figure
plt.figure(figsize=(10,7))

# Add title
plt.title("Relationship between sugarpercent and winpercent")

# simple scatter plot
sns.scatterplot(x=candy_data["sugarpercent"], y=candy_data["winpercent"])

# adding a regression line to that scatter plot (best fit of the data to check the dependences)
sns.regplot(x=candy_data["sugarpercent"], y=candy_data["winpercent"])

# Scatter plot showing the relationship between 'pricepercent', 'winpercent', and 'chocolate'

# Set the width and height of the figure
plt.figure(figsize=(10,7))

# Add title
plt.title("Relationship between pricepercent, winpercent, and chocolate")

# using the color-coded scatter plot
sns.scatterplot(x=candy_data["pricepercent"], y=candy_data["winpercent"], hue=candy_data["chocolate"])

# adding separate regression lines for color-coded plot using sns.lmplot to investigate the influence of chocolate
sns.lmplot(x="pricepercent", y="winpercent", hue="chocolate", data=candy_data)

# Scatter plot showing the relationship between 'chocolate' and 'winpercent'

# Set the width and height of the figure
plt.figure(figsize=(14,14))

# Add title
plt.title("Relationship between chocolate and winpercent")

# using sns.swarmplot command to plot dependence of 'winpercent' on 'chocolate'
sns.swarmplot(x=candy_data["chocolate"], y=candy_data["winpercent"])

#__________________________________________________________________________________________
# Distributions. Histograms. Kernel density estimate (KDE) plot.

# iris dataset

# Path of the file to read
iris_filepath = "input_data/iris.csv"

# Reading the file into a variable iris_data stting column "Id" as an index column
iris_data = pd.read_csv(iris_filepath, index_col="Id")

# ================ Histogram (based on counts) =============================

# Set the width and height of the figure
plt.figure(figsize=(10,7))

# Add title
plt.title("Distribution of Iris's Petal Length")

# building the histogram graph based on "Petal Length (cm)" column
sns.histplot(iris_data['Petal Length (cm)'])

# ================ Kernel density estimate (KDE) plot (smoothed histogram) =============================

# Set the width and height of the figure
plt.figure(figsize=(10,7))

# Add title
plt.title("Distribution of Iris's Petal Length")

# KDE plot 
sns.kdeplot(data=iris_data['Petal Length (cm)'], fill=True)

# ================ Two-dimensional (2D) KDE plot (smoothed histogram with counts based on two columns data) =============================

# Two-dimensional (2D) KDE plot based on "Petal Length (cm)" column data, and "Sepal Width (cm)" column data using sns.jointplot command
sns.jointplot(x=iris_data["Petal Length (cm)"], y=iris_data["Sepal Width (cm)"], kind="kde", space=1.1)

# Add title
plt.title("Distribution of Iris's Petal Length (cm)\nand Sepal Width (cm) (two-dimensional)")

# ================ Color-coded Histogram (based on counts) =============================

# The same dataset

# Set the width and height of the figure
plt.figure(figsize=(10,7))

# Add title
plt.title("Distribution of Iris's Petal Length for Different Species")


# The same histogram as before, but using different colors depending on specie value (column "Species")
sns.histplot(data=iris_data, x="Petal Length (cm)", hue="Species")

# ================ Color-coded Kernel density estimate (KDE) plot (smoothed histogram) =============================

# Set the width and height of the figure
plt.figure(figsize=(10,7))

# Add title
plt.title("Distribution of Iris's Petal Length for Different Species")

# KDE plot 
sns.kdeplot(data=iris_data, x="Petal Length (cm)", hue="Species", fill=True)

# ================ Two-dimensional (2D) Color-coded KDE plot (smoothed histogram with counts based on two columns data) =============================

# Two-dimensional (2D) KDE plot based on "Petal Length (cm)" column data, and "Sepal Width (cm)" column data using sns.jointplot command
sns.jointplot(data=iris_data, x="Petal Length (cm)", y="Sepal Width (cm)", kind="kde", hue="Species", space=2.1)

# Add title
plt.title("Distribution of Iris's Petal Length (cm)\nand Sepal Width (cm)\nfor Different Species (two-dimensional)")


