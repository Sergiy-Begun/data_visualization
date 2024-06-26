#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 17:39:55 2024

@author: sergiybegun
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

# A (synthetic) dataset of insurance charges. Scatter Plot.

# Path of the file to read
insurance_filepath = "input_data/insurance.csv"

# Read the file into a variable insurance_data
insurance_data = pd.read_csv(insurance_filepath)

# Set the width and height of the figure
plt.figure(figsize=(14,7))

# Add title
plt.title("Average game score by platform and genre")

# simple scatter plot
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'])

# adding a regression line to that scatter plot (best fit of the data to check the dependences)
sns.regplot(x=insurance_data['bmi'], y=insurance_data['charges'])



