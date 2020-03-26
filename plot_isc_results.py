import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

datadir = '/jukebox/norman/jamalw/Eternal_Sunshine/scripts/data/isc/'

music = np.load(datadir + 'music_group_rA1.npy')
no_music = np.load(datadir + 'no_music_group_rA1.npy')

music_iscs = music[~np.isnan(music)]
no_music_iscs = no_music[~np.isnan(no_music)]

# plot data and save figure
x = np.arange(2)
avgData = [np.mean(music_iscs),np.mean(no_music_iscs)]
semData = [stats.sem(music_iscs,axis=None,ddof=0),stats.sem(no_music_iscs,axis=None,ddof=0)]
plt.bar(x,avgData,yerr=semData)
plt.xticks(x,('music','no music'),fontsize=15)
plt.title('ISC for Full Movie (rA1)',fontsize=20)
plt.ylabel('ISC (r)',fontsize=15)
plt.tight_layout()
plt.savefig('isc_results_rA1')
