import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

datadir = '/tigress/epiazza/keyboard/results/isc/'

group = 'AM'
conds = ['I', '8B', '2B', '1B']


I = np.load(datadir + 'I_iscs_' + group + '.npy')
ISC_I = I[~np.isnan(I)]

8B = np.load(datadir + '8B_iscs_' + group + '.npy')
ISC_8B = 8B[~np.isnan(8B)]

2B = np.load(datadir + '2B_iscs_' + group + '.npy')
ISC_2B = 2B[~np.isnan(2B)]

1B = np.load(datadir + '1B_iscs_' + group + '.npy')
ISC_1B = 1B[~np.isnan(1B)]


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
