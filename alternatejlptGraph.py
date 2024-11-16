import pandas as pd
from matplotlib import pyplot as plt
import json


f = open('profile.json')
profile = json.load(f)
df = profile['level_progress_percs']
print(df)

YAxis = ['Vocab', 'Kanji', 'Grammar', 'Sentences', '']
XAxis = [profile['level_progress_percs']['vocab']['n5'], profile['level_progress_percs']['kanji']['n5'],profile['level_progress_percs']['grammar']['n5'],profile['level_progress_percs']['sent']['n5'], 0]

# Figure Size
fig, ax = plt.subplots(figsize =(9, 4))

# Horizontal Bar Plot
ax.barh(YAxis, XAxis)

# Remove axes splines
for s in ['top', 'bottom', 'left', 'right']:
    ax.spines[s].set_visible(False)

# Remove x, y Ticks
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
#ax.set_xticklabels(YAxis, fontsize=1, color='grey')
ax.set_yticklabels(YAxis, fontsize=10, color='white')

# Add padding between axes and labels
#ax.xaxis.set_tick_params(pad = 5)
#ax.yaxis.set_tick_params(pad = 10)

# Add x, y gridlines
"""ax.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)"""

# Show top values 
ax.invert_yaxis()

ax.set_facecolor('#201c1c')
#plt.figure(facecolor='#94F008')
#fig = plt.figure()
fig.patch.set_facecolor('#201c1c')

font1 = {'color':'white' }
font2 = {'color':'white','size':15}

plt.title("N5", fontdict= font2)



#ax.set_facecolor((1.0, 0.47, 0.42))

# Add annotation to bars
for i in ax.patches:
    plt.text(i.get_width()+0.2, i.get_y()+0.5, 
             str(round((i.get_width()), 2))+ '%',
             fontsize = 10, fontweight ='bold',
             color ='white') # add percent label here
    
colorsValue = []
for value in XAxis:
    if value <100:
        colorsValue.append('blue')
    else:
        colorsValue.append('green')

plt.barh(YAxis, XAxis, color = colorsValue)



# Show Plot
plt.show()