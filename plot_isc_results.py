import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

ROI = 'Precuneus'
group = 'AM'

datadir = '/tigress/epiazza/keyboard/results/isc_.01Hz/' + ROI +'/'

conds = ['1B', '2B', '8B', 'I']

ISC_1B = np.load(datadir + '1B_iscs_' + group + '.npy')
ISC_2B = np.load(datadir + '2B_iscs_' + group + '.npy')
ISC_8B = np.load(datadir + '8B_iscs_' + group + '.npy')
ISC_I = np.load(datadir + 'I_iscs_' + group + '.npy')


# plot data and save figure
x = np.arange(4)

avgData = [np.mean(ISC_1B),np.mean(ISC_2B),np.mean(ISC_8B),np.mean(ISC_I)]
semData = [stats.sem(ISC_1B,axis=None,ddof=0),stats.sem(ISC_2B,axis=None,ddof=0),stats.sem(ISC_8B,axis=None,ddof=0),stats.sem(ISC_I,axis=None,ddof=0)]

plt.bar(x,avgData,yerr=semData)
plt.xticks(x,('1B','2B','8B','I'),fontsize=15)
plt.title(['ISC Across Scrambled Conditions (' + ROI + ')'],fontsize=20)
plt.ylabel('ISC (r)',fontsize=15)
plt.tight_layout()
plt.savefig(datadir + 'isc_results_' + ROI + '_' + group)
