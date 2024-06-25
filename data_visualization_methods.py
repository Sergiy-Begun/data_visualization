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

# Line chart showing how data_for_investigation evolved over time 
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

# Bar chart showing average arrival delay for Spirit Airlines flights by month
sns.barplot(x=flight_data.index, y=flight_data['NK'])

# ================ HeatMap =============================

# Set the width and height of the figure
plt.figure(figsize=(14,7))

# Add title
plt.title("Average Arrival Delay for Each Airline, by Month")

# Add label for horizontal axis
plt.xlabel("Airline")

# Heatmap showing average arrival delay for each airline by month
sns.heatmap(data=flight_data, annot=True)
