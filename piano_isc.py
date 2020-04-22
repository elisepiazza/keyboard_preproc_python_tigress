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

ROI = 'AngularGyrus'

#group = 'AM'
#subjs = ['sub-103', 'sub-120', 'sub-123']

group = 'M'
subjs = ['sub-105', 'sub-117', 'sub-121', 'sub-122']


datadir = '/tigress/epiazza/keyboard/data/'
save_dir = '/tigress/epiazza/keyboard/results/isc/'

mask = nib.load('/tigress/epiazza/keyboard/rois/AngularGyrus_3mm_custom.nii.gz')
mask_size = mask.get_data()[mask.get_data()==1].shape[0]
condition_data = pd.read_csv('/tigress/epiazza/keyboard/data/Conditions.csv')

conds = ['I', '8B', '2B', '1B']
#conds = ['I_A', 'I_I']


TR = 1.7
high_pass = 0.01
nRuns = 18
nReps = 3
nTR = 148

# Structure data for brainiak isc function
for c in range(len(conds)):
    # Initialize data structure for each condition separately, which will go into ISC
    data = np.empty((nTR, mask_size, len(subjs)))  
    data_indvReps = np.empty((nTR, mask_size, nReps, len(subjs)))  
    for s in range(len(subjs)):
        # Select subject-specific column containing condition labels
        subj_col = condition_data.loc[:, subjs[s]]
        # Select indices corresponding to current condition
        idx = np.where(subj_col == conds[c])[0] + 1
        # Initialize structure for storing average run data across subjects
        avgRuns = np.empty((nTR,mask_size))
        Runs3D = np.empty((nTR,mask_size,nReps)) 
        for r in range(len(idx)):
            # Load run data 
            runData = nib.load(datadir + subjs[s] + '/clean_data/clean_data_run' + str(idx[r]) + '.nii.gz')
            # Mask data
            masked_data = apply_mask(runData, mask)
            # store masked data for each run separately
            Runs3D[:,:,r] = masked_data
        # Store rep-specific data for each subject
        data_indvReps[:,:,:,s] = Runs3D      
        # Store averaged run data for each subject separately
        data[:,:,s] = np.mean(Runs3D,axis=2)  

    #Save (voxel-averaged) rep-specific data
    avgData_indvReps = np.mean(data_indvReps,axis=1,keepdims=False)
    np.save(save_dir + ROI + '/' + conds[c] + '_avgData_indvReps_' + group, avgData_indvReps)   

    # Average over all voxels before feeding to ISC   
    avgData = np.mean(data,axis=1,keepdims=True) 
    # Run ISC!!!        
    iscs = isc(avgData, pairwise=False)
    # Save ISCs 
    np.save(save_dir + ROI + '/' + conds[c] + '_iscs_' + group, iscs) 

    #Remove 3rd (singleton) dim and save rep-averaged data
    avgData_tosave = np.squeeze(avgData) 
    np.savetxt(save_dir + ROI + '/' + conds[c] + '_avgData_' + group + '.txt', avgData_tosave, delimiter =',')
    np.save(save_dir + ROI + '/' + conds[c] + '_avgData_' + group, avgData_tosave) 
