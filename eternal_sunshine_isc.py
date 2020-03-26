import numpy as np
import nibabel as nib
import numpy.ma as ma
from scipy.stats import zscore
from isc_standalone import isc
from nilearn.masking import apply_mask
import matplotlib.pyplot as plt
from scipy import stats
from nilearn.signal import clean

# This script calls the brainiak isc and isfc function to perform full brain isc on music data.


# music group
music_subjs = ['sub-002','sub-003','sub-005','sub-008','sub-010','sub-011','sub-013','sub-015','sub-017','sub-019','sub-021','sub-023']

# no music group
no_music_subjs = ['sub-001','sub-004','sub-006','sub-007','sub-009','sub-012','sub-014','sub-016','sub-018','sub-020','sub-022']

datadir = '/jukebox/norman/jamalw/Eternal_Sunshine/data/bids/NormaL/Jamal/EternalSunshineBIDS/derivatives/fmriprep/'

fn_run1 = '_watch_run1_smoothed_3mm.nii.gz'
fn_run2 = '_watch_run2_smoothed_3mm.nii.gz' 

mask = nib.load('/jukebox/norman/jamalw/Eternal_Sunshine/data/nifti/rA1_mask_25mm.nii.gz')
mask_size = mask.get_data()[mask.get_data()==1].shape[0]

music_data = np.empty((6455,mask_size,len(music_subjs)))
no_music_data = np.empty((6455,mask_size,len(no_music_subjs)))

TR = 1
high_pass = 0.01

# Structure data for brainiak isc function (don't forget that first 3 TRs of second run are the last 3 seconds of run 1. This was used to help subjects reorient to the movie after their break).
for i in range(len(music_subjs)):
    data_run1 = zscore(apply_mask(datadir + music_subjs[i] + '/ses-01/func/' + music_subjs[i] + fn_run1, mask)[0:3240,:])
    data_run2 = zscore(apply_mask(datadir + music_subjs[i] + '/ses-01/func/' + music_subjs[i] + fn_run2, mask)[3:3218,:])
    data = np.vstack((data_run1,data_run2))
    ## Compute mean signal
    mu = data.mean(axis=0)
    ## Apply highpass data.
    data = clean(data, detrend=True, standardize=False, high_pass=high_pass, t_r=TR)
    ## Convert to percent signal change.
    music_data[:,:,i] = data

music_data_mean = np.mean(music_data,axis=1,keepdims=True)
music_iscs = isc(music_data_mean, pairwise=False)

for i in range(len(no_music_subjs)):
    data_run1 = zscore(apply_mask(datadir + no_music_subjs[i] + '/ses-01/func/' + no_music_subjs[i] + fn_run1, mask)[0:3240,:])
    data_run2 = zscore(apply_mask(datadir + no_music_subjs[i] + '/ses-01/func/' + no_music_subjs[i] + fn_run2, mask)[3:3218,:])
    data = np.vstack((data_run1,data_run2))
    ## Compute mean signal
    mu = data.mean(axis=0)
    ## Apply highpass data.
    data = clean(data, detrend=True, standardize=False, high_pass=high_pass, t_r=TR)
    ## Convert to percent signal change.
    no_music_data[:,:,i] = data
    
no_music_data_mean = np.mean(no_music_data,axis=1,keepdims=True)
no_music_iscs = isc(no_music_data_mean, pairwise=False)

# save isc data
print('Saving ISC Results')
save_dir = '/jukebox/norman/jamalw/Eternal_Sunshine/scripts/data/'
np.save(save_dir + 'isc/music_group_rA1',music_iscs)
np.save(save_dir + 'isc/no_music_group_rA1', no_music_iscs)
np.save(save_dir + 'subj_data/roi_data/music_group_rA1',music_data)
np.save(save_dir + 'subj_data/roi_data/no_music_group_rA1', no_music_data) 
