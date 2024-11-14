# example pulled from geeks for geeks 
# url here : https://www.geeksforgeeks.org/bar-plot-in-matplotlib/

# combine this example with a previous one.
# bars horizontal with labels for each, sort by jlpt and kanji
# export final graphic as an image and save to directory so can be pulled into frame.py


# importing packages 
import pandas as pd 
import matplotlib.pyplot as plt 
import json
import numpy as np

f = open('profile.json')
profile = json.load(f)
df = profile['level_progress_percs']
print(df)

data = {'Level': 
        ['N5 Vocab', 'N5 Kanji', 'N5 Grammar', 'N5 Sentences'], 
        'Percent': 
        [
        profile['level_progress_percs']['vocab']['n5'], 
        profile['level_progress_percs']['kanji']['n5'],
        profile['level_progress_percs']['grammar']['n5'],
        profile['level_progress_percs']['sent']['n5']
        ]
        }

data2 = {'Level': ['N5 Vocab' ], 'Percent':[profile['level_progress_percs']['vocab']['n5']] }

YAxis = ['N5 Vocab', 'N5 Kanji', 'N5 Grammar', 'N5 Sentences']
XAxis = [profile['level_progress_percs']['vocab']['n5'], profile['level_progress_percs']['kanji']['n5'],profile['level_progress_percs']['grammar']['n5'],profile['level_progress_percs']['sent']['n5']]

fig, ax = plt.subplots(figsize =(16, 9))

ax.barh(YAxis, XAxis)

for s in ['top', 'bottom', 'left', 'right']:
    ax.spines[s].set_visible(False)

ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')

ax.xaxis.set_tick_params(pad = 5)
ax.yaxis.set_tick_params(pad = 10)

# Add x, y gridlines
ax.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)

# Show top values 
ax.invert_yaxis()

# Add annotation to bars
for i in ax.patches:
    plt.text(i.get_width()+0.2, i.get_y()+0.5, 
             str(round((i.get_width()), 2)),
             fontsize = 10, fontweight ='bold',
             color ='grey')

# Add Plot Title
ax.set_title('Sports car and their price in crore',
             loc ='left', )

# Add Text watermark
fig.text(0.9, 0.15, 'Jeeteshgavande30', fontsize = 12,
         color ='grey', ha ='right', va ='bottom',
         alpha = 0.7)

# Show Plot
plt.show()

"""X_axis = np.arange(len(YAxis)) 

#plt.bar(X_axis + 0.2, XAxis, 0.4, label = 'N5') 
  
plt.xticks(X_axis, YAxis) 
plt.xlabel("Groups") 
plt.ylabel("Percent") 
plt.legend() 
plt.show() 
# view dataset 
#print(data)"""

