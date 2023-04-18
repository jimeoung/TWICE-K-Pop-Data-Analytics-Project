import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Load the dataset
df = pd.read_csv('twice_korean_singles_lines.csv')

# Group the DataFrame by member and sum the duration of their lines
lines_by_member = df.groupby(['vocal1'])['duration'].sum() + df.groupby(['vocal2'])['duration'].sum()

# Filter out the 'all' category
lines_by_member = lines_by_member.loc[lines_by_member.index != 'ALL']

# Sort the result in descending order
lines_by_member = lines_by_member.sort_values(ascending=False)

# Define the color gradient
colors = ['#FBCEB1', '#EF25AF']

# Create a LinearSegmentedColormap
cmap = mcolors.LinearSegmentedColormap.from_list("", colors)

# Plot the bar chart with the updated data
lines_by_member.plot(kind='bar', color=cmap(lines_by_member/max(lines_by_member)))
plt.title('TWICE Members by Line Duration')
plt.xlabel('Member')
plt.ylabel('Duration (seconds)')
plt.show()
