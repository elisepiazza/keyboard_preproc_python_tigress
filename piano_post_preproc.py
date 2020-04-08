import nibabel as nib
from nilearn import image
from nilearn.signal import clean
import sys
import pandas as pd
import numpy as np

s = int(sys.argv[1])


datadir = "/tigress/epiazza/keyboard/data/"

subj_ids = ['sub-122', 'sub-123']
#subj_ids = ['sub-103', 'sub-105', 'sub-108', 'sub-117', 'sub-120', 'sub-121']

task_fn1 = '_ses-01_task-keyboard_run-'
task_fn2 = '_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz'

mask_fn_suffix = '_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz'

confounds_suffix = '_desc-confounds_regressors.tsv'

# high pass filter data
TR = 1.7
high_pass = 0.01
numRuns = 18

for s in range(len(subj_ids)):
    for r in range(numRuns):
        if r < 9:
            # load epi data 
            data = nib.load(datadir + subj_ids[s] + '/' + subj_ids[s] + task_fn1 + str(0)+ str(r+1) + task_fn2)
            # load confounds
            dfObj = pd.read_csv(datadir + subj_ids[s] + '/' + subj_ids[s] + task_fn1 + str(0) + str(r+1) + confounds_suffix, sep='\t')
            # load mask
            mask_img = nib.load(datadir + subj_ids[s] + '/' + subj_ids[s] + task_fn1 + str(0) + str(r+1) + mask_fn_suffix)
        elif r >= 9:
            # load epi data
            data = nib.load(datadir + subj_ids[s] + '/' + subj_ids[s] + task_fn1 + str(r+1) + task_fn2)
            # load confounds
            dfObj = pd.read_csv(datadir + subj_ids[s] + '/' + subj_ids[s] + task_fn1 + str(r+1) + confounds_suffix, sep='\t')
            # load mask
            mask_img = nib.load(datadir + subj_ids[s] + '/' + subj_ids[s] + task_fn1 + str(r+1) + mask_fn_suffix)
          
        # convert confounds dataframe to values
        confound_regs = dfObj.loc[ : , ['a_comp_cor_00', 'a_comp_cor_01', 'a_comp_cor_02', 'a_comp_cor_03','a_comp_cor_04', 'a_comp_cor_05','trans_x', 'trans_y', 'trans_z','rot_x','rot_y','rot_z'] ].values[6:]

        # grab mask indices and mask active voxels only from epi
        indices = np.where(mask_img.get_data() > 0 )
        masked_data = data.get_data()[indices][:,6:].T

        # Apply highpass data.
        clean_data = clean(masked_data, detrend=True, standardize=True, confounds=confound_regs, high_pass=high_pass, t_r=TR)

        # reshape data back into 3D
        image_map = np.zeros_like(data.get_data()[:,:,:,6:])
        image_map[indices] = clean_data.T        
 
        # convert to nifti object
        affine = data.affine
        maxval = np.max(image_map)
        minval = np.min(image_map)
        img = nib.Nifti1Image(image_map, affine=affine)
        img.header['cal_min'] = minval
        img.header['cal_max'] = maxval

        #save preprocessed data
        nib.save(img,datadir + subj_ids[s] + '/clean_data/clean_data_run' + str(r+1) + '.nii.gz')

		




