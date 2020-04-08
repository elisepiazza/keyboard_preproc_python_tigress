import numpy as np
import nibabel as nib
import numpy.ma as ma
from scipy.stats import zscore
from isc_standalone import isc
from nilearn.masking import apply_mask
from nilearn.masking import compute_epi_mask
import matplotlib.pyplot as plt
from scipy import stats
from nilearn.signal import clean
import pandas as pd

# This script calls the brainiak isc and isfc function to perform full brain isc on keyboard data.

#subjs = ['sub-103','sub-105','sub-108','sub-117','sub-120','sub-121', 'sub-122', 'sub-123']
#groups = ['AM', 'M', 'M', 'M', 'AM', 'M', 'M', 'AM']

subjs = ['sub-103','sub-105']

datadir = '/tigress/epiazza/keyboard/data/'
save_dir = '/tigress/epiazza/keyboard/results/isc/'

mask = nib.load('/tigress/epiazza/keyboard/rois/a1plus_3mm_bin.nii.gz')
mask_size = mask.get_data()[mask.get_data()==1].shape[0]
condition_data = pd.read_csv('/tigress/epiazza/keyboard/data/Conditions.csv')

conds = ['I', '8B', '2B', '1B']


TR = 1.7
high_pass = 0.01
nRuns = 18
nTR = 148

# Structure data for brainiak isc function
for c in range(len(conds)):
    # Initialize data structure for each condition separately, which will go into ISC
    data = np.empty((nTR, mask_size, len(subjs)))    
    for s in range(len(subjs)):
        # Select subject-specific column containing condition labels
        subj_col = condition_data.loc[:, subjs[s]]
        # Select indices corresponding to current condition
        idx = np.where(subj_col == conds[c])[0] + 1
        # Initialize structure for storing average run data across subjects
        avgRuns = np.empty((nTR,mask_size))    
        for r in range(len(idx)):
            # Load run data 
            runData = nib.load(datadir + subjs[s] + '/clean_data/clean_data_run' + str(idx[r]) + '.nii.gz')
            # Mask data
            masked_data = apply_mask(runData, mask)
            # Average current run into existing data structure
            avgRuns += masked_data/len(idx)
        # Store average run data for each subject separately
        data[:,:,s] = avgRuns       
    # Average over all voxels before feeding to ISC   
    avgData = np.mean(data,axis=1,keepdims=True) 
    # Run ISC!!!        
    iscs = isc(avgData, pairwise=False)
    # Save ISCs 
    np.save(save_dir + conds[c] + '_iscs',iscs) 

