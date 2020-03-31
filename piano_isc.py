import numpy as np
import nibabel as nib
import numpy.ma as ma
from scipy.stats import zscore
from isc_standalone import isc
from nilearn.masking import apply_mask
import matplotlib.pyplot as plt
from scipy import stats
from nilearn.signal import clean

# This script calls the brainiak isc and isfc function to perform full brain isc on keyboard data.


# subjs
subjs = ['sub-103','sub-105','sub-108','sub-008','sub-117','sub-120','sub-121']

#datadir = '/jukebox/hasson/elise/fMRI/fmriprep/keyboard/data/bids/derivatives/fmriprep/'
datadir = '/tigress/epiazza/keyboard/data/'

#fn_run = 'clean_data_run_smoothed_3mm.nii.gz'

mask = nib.load('/jukebox/norman/jamalw/Eternal_Sunshine/data/nifti/rA1_mask_25mm.nii.gz')
mask_size = mask.get_data()[mask.get_data()==1].shape[0]

data = np.empty((6455,mask_size,len(subjs)))

TR = 1
high_pass = 0.01
nRuns = 18

# Structure data for brainiak isc function (don't forget that first 3 TRs of second run are the last 3 seconds of run 1. This was used to help subjects reorient to the movie after their break).
for i in range(len(subjs)):
    for r in range(nRuns)
    data = zscore(apply_mask(datadir + subjs[i] + '/clean_data/clean_data_run' + str(r) + '.nii.gz', mask)[0:3240,:])
    #data = zscore(apply_mask(datadir + subjs[i] + '/ses-01/func/' + subjs[i] + 'clean_data_run' , mask)[0:3240,:])
    #data = np.vstack((data_run1,data_run2))
    ## Compute mean signal
    mu = data.mean(axis=0)
    ## Apply highpass data.
    data = clean(data, detrend=True, standardize=False, high_pass=high_pass, t_r=TR)
    ## Convert to percent signal change.
    data[:,:,i] = data

data_mean = np.mean(data,axis=1,keepdims=True)
iscs = isc(data_mean, pairwise=False)

# save isc data
print('Saving ISC Results')
save_dir = '/jukebox/norman/jamalw/Eternal_Sunshine/scripts/data/'
np.save(save_dir + 'isc/rA1',iscs)
np.save(save_dir + 'subj_data/roi_data/rA1',data)
