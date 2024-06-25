#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 17:39:55 2024

@author: sergiybegun
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Path to the data
data_filepath = "input_data/fifa.csv"

# Read the data from file parsing the date of events as a date column, and making the Date column as an index column
data_for_investigation = pd.read_csv(data_filepath, index_col="Date", parse_dates=True)

# Set the width and height of the figure
plt.figure(figsize=(16,6))

# Line chart showing how data_for_investigation evolved over time 
sns.lineplot(data=data_for_investigation)