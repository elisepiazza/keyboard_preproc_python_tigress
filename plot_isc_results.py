import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

ROI = 'vmPFC'
group = 'M'

datadir = '/tigress/epiazza/keyboard/results/isc/' + ROI +'/'

conds = ['I', '8B', '2B', '1B']


ISC_I = np.load(datadir + 'I_iscs_' + group + '.npy')
ISC_8B = np.load(datadir + '8B_iscs_' + group + '.npy')
ISC_2B = np.load(datadir + '2B_iscs_' + group + '.npy')
ISC_1B = np.load(datadir + '1B_iscs_' + group + '.npy')


# plot data and save figure
x = np.arange(4)
avgData = [np.mean(ISC_I),np.mean(ISC_8B),np.mean(ISC_2B),np.mean(ISC_1B)]
semData = [stats.sem(ISC_I,axis=None,ddof=0),stats.sem(ISC_8B,axis=None,ddof=0),stats.sem(ISC_2B,axis=None,ddof=0),stats.sem(ISC_1B,axis=None,ddof=0)]
plt.bar(x,avgData,yerr=semData)
plt.xticks(x,('I','8B','2B','1B'),fontsize=15)
plt.title(['ISC Across Scrambled Conditions (' + ROI + ')'],fontsize=20)
plt.ylabel('ISC (r)',fontsize=15)
plt.tight_layout()
plt.savefig(datadir + 'isc_results_' + ROI + '_' + group)
