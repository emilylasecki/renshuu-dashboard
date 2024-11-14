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


X_axis = np.arange(len(YAxis)) 

plt.bar(X_axis + 0.2, XAxis, 0.4, label = 'N5') 
  
plt.xticks(X_axis, YAxis) 
plt.xlabel("Groups") 
plt.ylabel("Percent") 
plt.legend() 
plt.show() 
# view dataset 
#print(data) 

