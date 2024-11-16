import matplotlib.pyplot as plt
import json
import pandas as pd


f = open('profile.json')
profile = json.load(f)
df = profile['level_progress_percs']
print(df)

YAxis = ['Vocab', 'Kanji', 'Grammar', 'Sentences']
XAxis = [profile['level_progress_percs']['vocab']['n5'], profile['level_progress_percs']['kanji']['n5'],profile['level_progress_percs']['grammar']['n5'],profile['level_progress_percs']['sent']['n5']]
XAxis2 = [profile['level_progress_percs']['vocab']['n4'], profile['level_progress_percs']['kanji']['n4'],profile['level_progress_percs']['grammar']['n4'],profile['level_progress_percs']['sent']['n4']]
XAxis3 = [profile['level_progress_percs']['vocab']['n3'], profile['level_progress_percs']['kanji']['n3'],profile['level_progress_percs']['grammar']['n3'],profile['level_progress_percs']['sent']['n3']]
XAxis4 = [profile['level_progress_percs']['vocab']['n2'], profile['level_progress_percs']['kanji']['n2'],profile['level_progress_percs']['grammar']['n2'],profile['level_progress_percs']['sent']['n2']]
XAxis5 = [profile['level_progress_percs']['vocab']['n1'], profile['level_progress_percs']['kanji']['n1'],profile['level_progress_percs']['grammar']['n1'],profile['level_progress_percs']['sent']['n1']]

fid, axs = plt.subplots(5)

axs[0].invert_yaxis()
axs[1].invert_yaxis()
axs[2].invert_yaxis()
axs[3].invert_yaxis()
axs[4].invert_yaxis()



axs[0].barh(YAxis, XAxis)
axs[1].barh(YAxis, XAxis2)
axs[2].barh(YAxis, XAxis3)
axs[3].barh(YAxis, XAxis4)
axs[4].barh(YAxis, XAxis5)

for s in ['top', 'bottom', 'left', 'right']:
    axs[0].spines[s].set_visible(False)
    axs[1].spines[s].set_visible(False)
    axs[2].spines[s].set_visible(False)
    axs[3].spines[s].set_visible(False)
    axs[4].spines[s].set_visible(False)

axs[0].set_facecolor('#201c1c')
fid.patch.set_facecolor('#201c1c')

plt.show()