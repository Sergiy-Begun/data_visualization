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

# changing the limit of warning due to the big number of graphs
plt.rcParams['figure.max_open_warning'] = 50

# Fifa Data Set. Linear Chart Graph

# Path to the data
data_filepath = "input_data/fifa.csv"

# Read the data from file parsing the date of events as a date column, and making the Date column as an index column
data_for_investigation = pd.read_csv(data_filepath, index_col="Date", parse_dates=True)

graph1= plt

# Set the width and height of the figure
graph1.figure(figsize=(16,6))

# Setting the title for the chart
graph1.title("Historical FIFA rankings for six countries")

# Add label for horizontal axis
graph1.xlabel("Date")

# Add label for vertical axis
graph1.ylabel("Rank")

# Line chart showing how data_for_investigation evolved over time 
graph1.axes = sns.lineplot(data=data_for_investigation)

# saving resulting graph to the file
graph1.savefig("output_data/graph1.png")

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

# creating graph object
graph2 = plt

# Set the width and height of the figure
graph2.figure(figsize=(16,6))

# Setting the title for the chart
graph2.title("The number of visitors to each museum over time")

# Add label for horizontal axis
graph2.xlabel("Date")

# Add label for vertical axis
graph2.ylabel("The number of visitors per month")

# Line chart showing how museum_data evolved over time creating inside graph object graph2
graph2.axes = sns.lineplot(data=museum_data)

# saving resulting graph to the file
graph2.savefig("output_data/graph2.png")

#__________________________________________________________________________________________

# Flights Data Set. BarPlot & HeatMap Graphs.

# ================ BarPlot =============================

# Path of the file to read
flight_filepath = "input_data/flight_delays.csv"

# Read the file into a variable flight_data, and setting Month column as an index
flight_data = pd.read_csv(flight_filepath, index_col="Month")

# creating graph object
graph3 = plt

# Set the width and height of the figure
graph3.figure(figsize=(10,6))

# Add title
graph3.title("Average Arrival Delay for Spirit Airlines Flights, by Month")

# Bar chart showing average arrival delay for Spirit Airlines flights by month
graph3.axes = sns.barplot(x=flight_data.index, y=flight_data['NK'])

# Add label for vertical axis
graph3.ylabel("Arrival delay (in minutes)")

# saving resulting graph to the file
graph3.savefig("output_data/graph3.png")


# ================ HeatMap =============================

# creating graph object
graph4 = plt

# Set the width and height of the figure
graph4.figure(figsize=(14,7))

# Add title
graph4.title("Average Arrival Delay for Each Airline, by Month")

# Add label for horizontal axis
graph4.xlabel("Airline")

# Heatmap showing average arrival delay for each airline by month
graph4.axes = sns.heatmap(data=flight_data, annot=True)

# saving resulting graph to the file
graph4.savefig("output_data/graph4.png")

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

# creating graph object
graph5 = plt

# Set the width and height of the figure
graph5.figure(figsize=(35,10))

# Add title
graph5.title("Average score for racing games by platform")

# Bar chart showing average score for racing games by platform
graph5.axes = sns.barplot(x=ign_data.index, y=ign_data['Racing'])

# Add label for vertical axis
graph5.ylabel("Score Value")

# saving resulting graph to the file
graph5.savefig("output_data/graph5.png")


# ================ HeatMap =============================

# Heatmap showing average game score by platform and genre

# creating graph object
graph6 = plt

# Set the width and height of the figure
graph6.figure(figsize=(14,7))

# Add title
graph6.title("Average game score by platform and genre")

# Add label for horizontal axis
graph6.xlabel("Platform")

# Heatmap showing average game score by platform and genre
graph6.axes = sns.heatmap(data=ign_data, annot=True)

# saving resulting graph to the file
graph6.savefig("output_data/graph6.png")

#__________________________________________________________________________________________

# A (synthetic) dataset of insurance charges. Scatter Plot. Color-coded scatter plots.
# Scatter plots for categorical variables

# ================ Scatter Plot =============================

# Path of the file to read
insurance_filepath = "input_data/insurance.csv"

# Read the file into a variable insurance_data
insurance_data = pd.read_csv(insurance_filepath)

# creating graph object
graph7 = plt

# Set the width and height of the figure
graph7.figure(figsize=(14,7))

# Add title
graph7.title("Insurance charges dependence on body mass index (BMI)")

# simple scatter plot
graph7.axes = sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'])

# adding a regression line to that scatter plot (best fit of the data to check the dependences) as a subplot of current axes
graph7.subplot = sns.regplot(x=insurance_data['bmi'], y=insurance_data['charges'])

# saving resulting graph to the file
graph7.savefig("output_data/graph7.png")

# ================ Color-coded scatter plots =============================

# Using the same data set

# creating graph object
graph8 = plt

# Set the width and height of the figure
graph8.figure(figsize=(10,7))

# Add title
graph8.title("Insurance charges dependence on body mass index (BMI)")

# use different color for data depending of smoker value ("yes" or "not", 
# could be other color if, for example, smoker value would be "unknown" or something else)
graph8.axes = sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'], hue=insurance_data['smoker'])

# adding separate regression lines for data of smokers and no-smokers using sns.lmplot
graph8.subplot = sns.lmplot(x="bmi", y="charges", hue="smoker", data=insurance_data)

# saving resulting graph to the file
graph8.savefig("output_data/graph8.png")

# ================ Scatter plots for categorical variables =============================

# Using the same data set

# creating graph object
graph9 = plt

# Set the width and height of the figure
graph9.figure(figsize=(14,14))

# Add title
graph9.title("Insurance charges dependence on smoking habits")

# using sns.swarmplot command to plot dependence of charges on smoking habits
graph9.axes = sns.swarmplot(x=insurance_data['smoker'], y=insurance_data['charges'])

# saving resulting graph to the file
graph9.savefig("output_data/graph9.png")

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

# creating graph object
graph10 = plt

# Set the width and height of the figure
graph10.figure(figsize=(10,7))

# Add title
graph10.title("Relationship between sugarpercent and winpercent")

# simple scatter plot
graph10.axes = sns.scatterplot(x=candy_data["sugarpercent"], y=candy_data["winpercent"])

# adding a regression line to that scatter plot (best fit of the data to check the dependences)
graph10.subplot = sns.regplot(x=candy_data["sugarpercent"], y=candy_data["winpercent"])

# saving resulting graph to the file
graph10.savefig("output_data/graph10.png")

# Scatter plot showing the relationship between 'pricepercent', 'winpercent', and 'chocolate'

# creating graph object
graph11 = plt

# Set the width and height of the figure
graph11.figure(figsize=(10,7))

# Add title
graph11.title("Relationship between pricepercent, winpercent, and chocolate")

# using the color-coded scatter plot
graph11.axes = sns.scatterplot(x=candy_data["pricepercent"], y=candy_data["winpercent"], hue=candy_data["chocolate"])

# adding separate regression lines for color-coded plot using sns.lmplot to investigate the influence of chocolate
graph11.subplot = sns.lmplot(x="pricepercent", y="winpercent", hue="chocolate", data=candy_data)

# saving resulting graph to the file
graph11.savefig("output_data/graph11.png")

# Scatter plot showing the relationship between 'chocolate' and 'winpercent'

# creating graph object
graph12 = plt

# Set the width and height of the figure
graph12.figure(figsize=(14,14))

# Add title
graph12.title("Relationship between chocolate and winpercent")

# using sns.swarmplot command to plot dependence of 'winpercent' on 'chocolate'
graph12.axes = sns.swarmplot(x=candy_data["chocolate"], y=candy_data["winpercent"])

# saving resulting graph to the file
graph12.savefig("output_data/graph12.png")

#__________________________________________________________________________________________
# Distributions. Histograms. Kernel density estimate (KDE) plot.
# Two-dimensional (2D) KDE plot (smoothed histogram with counts based on two columns data)
# Color-coded plots

# iris dataset

# Path of the file to read
iris_filepath = "input_data/iris.csv"

# Reading the file into a variable iris_data stting column "Id" as an index column
iris_data = pd.read_csv(iris_filepath, index_col="Id")

# ================ Histogram (based on counts) =============================

# creating graph object
graph13 = plt

# Set the width and height of the figure
graph13.figure(figsize=(10,7))

# Add title
graph13.title("Distribution of Iris's Petal Length")

# building the histogram graph based on "Petal Length (cm)" column
graph13.axes = sns.histplot(iris_data['Petal Length (cm)'])

# saving resulting graph to the file
graph13.savefig("output_data/graph13.png")

# ================ Kernel density estimate (KDE) plot (smoothed histogram) =============================

# creating graph object
graph14 = plt

# Set the width and height of the figure
graph14.figure(figsize=(10,7))

# Add title
graph14.title("Distribution of Iris's Petal Length")

# KDE plot 
graph14.axes = sns.kdeplot(data=iris_data['Petal Length (cm)'], fill=True)

# saving resulting graph to the file
graph14.savefig("output_data/graph14.png")

# ================ Two-dimensional (2D) KDE plot (smoothed histogram with counts based on two columns data) =============================

# creating graph object
graph15 = plt

# Two-dimensional (2D) KDE plot based on "Petal Length (cm)" column data, and "Sepal Width (cm)" column data using sns.jointplot command
graph15.axes = sns.jointplot(x=iris_data["Petal Length (cm)"], y=iris_data["Sepal Width (cm)"], kind="kde", space=1.1)

# Add title
graph15.title("Distribution of Iris's Petal Length (cm)\nand Sepal Width (cm) (two-dimensional)")

# saving resulting graph to the file
graph15.savefig("output_data/graph15.png")

# ================ Color-coded Histogram (based on counts) =============================

# The same dataset

# creating graph object
graph16 = plt

# Set the width and height of the figure
graph16.figure(figsize=(10,7))

# Add title
graph16.title("Distribution of Iris's Petal Length for Different Species")

# The same histogram as before, but using different colors depending on specie value (column "Species")
graph16.axes = sns.histplot(data=iris_data, x="Petal Length (cm)", hue="Species")

# saving resulting graph to the file
graph16.savefig("output_data/graph16.png")

# ================ Color-coded Kernel density estimate (KDE) plot (smoothed histogram) =============================

# creating graph object
graph17 = plt

# Set the width and height of the figure
graph17.figure(figsize=(10,7))

# Add title
graph17.title("Distribution of Iris's Petal Length for Different Species")

# KDE plot 
graph17.axes = sns.kdeplot(data=iris_data, x="Petal Length (cm)", hue="Species", fill=True)

# saving resulting graph to the file
graph17.savefig("output_data/graph17.png")

# ================ Two-dimensional (2D) Color-coded KDE plot (smoothed histogram with counts based on two columns data) =============================

# creating graph object
graph18 = plt

# Two-dimensional (2D) KDE plot based on "Petal Length (cm)" column data, and "Sepal Width (cm)" column data using sns.jointplot command
graph18.axes = sns.jointplot(data=iris_data, x="Petal Length (cm)", y="Sepal Width (cm)", kind="kde", hue="Species", space=2.1)

# Add title
graph18.title("Distribution of Iris's Petal Length (cm)\nand Sepal Width (cm)\nfor Different Species (two-dimensional)")

# saving resulting graph to the file
graph18.savefig("output_data/graph18.png")

#__________________________________________________________________________________________
# Distributions. Histograms. Kernel density estimate (KDE) plot.
# Two-dimensional (2D) KDE plot (smoothed histogram with counts based on two columns data)
# Color-coded plots

# cancer dataset

# Path of the files to read
cancer_filepath = "input_data/cancer.csv"

# Fill in the line below to read the file into a variable cancer_data
cancer_data = pd.read_csv(cancer_filepath, index_col="Id")

# In the first five rows of the data, what is the largest value for 'Perimeter (mean)'?
max_perim = cancer_data.head()["Perimeter (mean)"].max()

print("The largest value for \'Perimeter (mean)\' in the first five rows of the data is ", max_perim)

# What is the value for 'Radius (mean)' for the tumor with Id 8510824?
mean_radius = cancer_data[(cancer_data.index == 8510824)]["Radius (mean)"].iloc[0]

print("The value for \'Radius (mean)\' for the tumor with Id 8510824 is ", mean_radius)

# Histograms of Area (mean) for benign and maligant tumors

# Column ('Diagnosis') classifies tumors as either benign (which appears in the dataset as B) or malignant (M)

# creating graph object
graph19 = plt

# Set the width and height of the figure
graph19.figure(figsize=(10,10))

# Add title
graph19.title("Histograms of Area (mean) for benign and maligant tumors")

# building the color-coded histogram with different colors for different diagnosis
graph19.axes = sns.histplot(data=cancer_data, x="Area (mean)", hue="Diagnosis")

# saving resulting graph to the file
graph19.savefig("output_data/graph19.png")

# KDE plot that show the distribution in values for 'Radius (worst)'
# separately for both benign and malignant tumors

# creating graph object
graph20 = plt

# Set the width and height of the figure
graph20.figure(figsize=(10,10))

# Add title
graph20.title("Distribution in values for \'Radius (worst)\' for benign and maligant tumors")

# building color coded KDE plot with different colors for different diagnosis
graph20.axes = sns.kdeplot(data=cancer_data, x="Radius (worst)", hue="Diagnosis", fill=True)

# saving resulting graph to the file
graph20.savefig("output_data/graph20.png")

#__________________________________________________________________________________________
# Changing Graph Styles

# there are five styles of graph representation using seaborn:  (1)"darkgrid", (2)"whitegrid", (3)"dark", (4)"white", and (5)"ticks

# Dataset spotify

# Path of the file to read
spotify_filepath = "input_data/spotify.csv"

# Read the file into a variable spotify_data
spotify_data = pd.read_csv(spotify_filepath, index_col="Date", parse_dates=True)

# creating graph object
graph21 = plt

# Change the style of the seaborn objects
sns.set_style("dark")

# Set the width and height of the figure
graph21.figure(figsize=(12,6))

# Add title
graph20.title("Demonstration of Seaborn's Dark style with Spotify Dataset")

# building similar line chart using dark style of seaborn object
graph21.axes = sns.lineplot(data=spotify_data)

# saving resulting graph to the file
graph21.savefig("output_data/graph20.png")


