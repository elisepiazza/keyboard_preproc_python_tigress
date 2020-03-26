import nibabel as nib
from nilearn import image
from nilearn.signal import clean
import sys
import pandas as pd
import numpy as np

s = int(sys.argv[1])


datadir = "/home/epiazza/keyboard/data/"

subj_ids = ['sub-121', 'sub-120']

task_fn1 = '_ses-01_task-keyboard_run-'
task_fn2 = '_space-MNI152NLin2009cAsym_desc-preproc_bold.nii.gz'

confounds_suffix = '_desc-confounds_regressors.tsv'

# high pass filter data
TR = 1.7
high_pass = 0.01
numRuns = 18

for s in range(len(subj_ids)):
    for r in range(numRuns):
        if r < 10:
            data = nib.load(datadir + subj_ids[s] + '/' + subj_ids[s] + task_fn1 + str(0)+ str(r+1) + task_fn2)
            dfObj = pd.read_csv(datadir + subj_ids[s] + '/' + subj_ids[s] + task_fn1 + str(0) + str(r+1) + confounds_suffix, sep='\t')
        elif r >= 10:
            data = nib.load(datadir + subj_ids[s] + '/' + subj_ids[s] + task_fn1 + str(r+1) + task_fn2)
            dfObj = pd.read_csv(subj_ids[s] + task_fn1 + str(r+1) + confounds_suffix, sep='\t')

        confound_regs = dfObj.loc[ : , ['a_comp_cor_00', 'a_comp_cor_01', 'a_comp_cor_02', 'a_comp_cor_03','a_comp_cor_04', 'a_comp_cor_05','trans_x', 'trans_y', 'trans_z','rot_x','rot_y','rot_z'] ].values
 
        data_reshaped = np.reshape(data.get_data(),(65*77*65,data.get_data().shape[3])).T         
 
        # Apply highpass data.
        clean_data = clean(data_reshaped, detrend=True, standardize=True, confounds=confound_regs, high_pass=high_pass, t_r=TR)

        # reshape data back into 3D
        data4D = np.reshape(clean_data.T,(65,77,65,data.get_data().shape[3]))
      
        # convert to nifti object
        affine = data.affine
        maxval = np.max(data4D)
        minval = np.min(data4D)
        img = nib.Nifti1Image(data4D, affine=affine)

        #save preprocessed data
        nib.save(img,datadir + subj_ids[s] + '/clean_data/clean_data_run' + str(r+1) + '.nii.gz')

        x = 10        
		




