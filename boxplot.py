import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read in the dataset
df = pd.read_csv("twice_korean_singles_lines.csv")

# Group the data by song_name and member to sum up the durations
df_grouped = df.groupby(["song_name", "vocal1"])["duration"].sum().reset_index()

# Calculate the median duration for each member
medians = df_grouped.groupby("vocal1")["duration"].median()

# Sort the medians in descending order
medians_sorted = medians.sort_values(ascending=False)

# Create a dictionary to store the data for each member, ordered by median
data = {}
for member in medians_sorted.index:
    data[member] = df_grouped.loc[df_grouped["vocal1"] == member]["duration"]

# Create a boxplot using matplotlib library with custom colors for median, boxplot, and outliers
fig, ax = plt.subplots()
ax.boxplot(data.values(), patch_artist=True, boxprops=dict(facecolor='#EF25AF'), 
           medianprops=dict(color='k'), whiskerprops=dict(color='k'), 
           capprops=dict(color='k'), flierprops=dict(markerfacecolor='#FBCEB1'))
ax.set_xticklabels(data.keys())
ax.set_ylabel("Duration (seconds)")
ax.set_title("Member Duration Distribution")

plt.show()


