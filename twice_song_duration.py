import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# read in the dataset
df = pd.read_csv('twice_korean_singles_lines.csv')

# get a list of all the unique song names in the dataset
song_names = df['song_name'].unique()

# define the color map
color_map = mcolors.LinearSegmentedColormap.from_list('custom', ['#FBCEB1', '#EF25AF'], N=10)

# loop through each song name
for song_name in song_names:
    # create a dataframe for the current song
    song_df = df[df['song_name'] == song_name]
    
    # get the sum of durations for each member
    member_durations = song_df.groupby('vocal1')['duration'].sum().sort_values(ascending=False)
    
    # create a bar chart of the line distribution for the current song
    ax = member_durations.plot(kind='bar', color=color_map(member_durations.values/max(member_durations.values)))
    
    # modify the title to add spaces before capital letters (except for "TT")
    if song_name != "TT":
        title = ''.join([' ' + char if char.isupper() or char == '&' else char for char in song_name]).lstrip()
    else:
        title = song_name
    
    ax.set_title(title)
    ax.set_xlabel('Member')
    ax.set_ylabel('Duration (seconds)')
    plt.show()
