import pandas as pd
from matplotlib import pyplot as plt
import json


f = open('profile.json')
profile = json.load(f)
df = profile['level_progress_percs']
print(df)

YAxis = ['Vocab', 'Kanji', 'Grammar', 'Sentences']
XAxis = [profile['level_progress_percs']['vocab']['n5'], profile['level_progress_percs']['kanji']['n5'],profile['level_progress_percs']['grammar']['n5'],profile['level_progress_percs']['sent']['n5']]

XAxis2 = [profile['level_progress_percs']['vocab']['n4'], profile['level_progress_percs']['kanji']['n4'],profile['level_progress_percs']['grammar']['n4'],profile['level_progress_percs']['sent']['n4']]

fig, (ax1, ax2) = plt.subplots(2)


ax1.barh(YAxis, XAxis)

for s in ['top', 'bottom', 'left', 'right']:
    ax1.spines[s].set_visible(False)

ax1.xaxis.set_ticks_position('none')
ax1.yaxis.set_ticks_position('none')
ax1.set_xticklabels(YAxis, fontsize=1, color='#201c1c')
ax1.set_yticklabels(YAxis, fontsize=10, color='white')


ax1.invert_yaxis()

ax1.set_facecolor('#201c1c')
fig.patch.set_facecolor('#201c1c')

font1 = {'color':'white' }
font2 = {'color':'white','size':15}

plt.title("N5", fontdict= font2)

for i in ax1.patches:
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


#plt.barh(YAxis, XAxis, color = colorsValue)

# plot 2!
#fig, ax2 = plt.subplots(figsize =(9, 4))

ax2.barh(YAxis, XAxis)

for s in ['top', 'bottom', 'left', 'right']:
    ax1.spines[s].set_visible(False)

ax2.xaxis.set_ticks_position('none')
ax2.yaxis.set_ticks_position('none')
ax2.set_xticklabels(YAxis, fontsize=1, color='#201c1c')
ax2.set_yticklabels(YAxis, fontsize=10, color='white')

ax2.invert_yaxis()

ax2.set_facecolor('grey')

for i in ax2.patches:
    plt.text(i.get_width()+0.2, i.get_y()+0.5, 
             str(round((i.get_width()), 2))+ '%',
             fontsize = 10, fontweight ='bold',
             color ='white') # add percent label here

for value in XAxis:
    if value <100:
        colorsValue.append('blue')
    else:
        colorsValue.append('green')
plt.barh(YAxis, XAxis, color = colorsValue)

# Show Plot
plt.show()

"""fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
ax1.plot(x, y)
ax2.plot(x, -y)"""