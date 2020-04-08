import numpy as np
import sys
import nibabel as nib

subjs = ['sub-103','sub-105','sub-108', 'sub-117', 'sub-120', 'sub-121', 'sub-122', 'sub-123']

task_fn = '_ses-01_task-keyboard_run-'
mask_fn_suffix = '_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz'

datadir = '/tigress/epiazza/keyboard/data/'

mni_brain = nib.load('/tigress/epiazza/keyboard/rois/MNI152_T1_3mm_brain.nii.gz')

custom_mask = np.zeros_like(mni_brain.get_data())

numRuns = 18

numSubjsRuns = len(subjs) * numRuns

for s in range(len(subjs)):
    # load subj data for each run separately
    for r in range(numRuns):
        if r < 9:
            # load mask
            mask_data = nib.load(datadir + subjs[s] + '/' + subjs[s] + task_fn + str(0) + str(r+1) + mask_fn_suffix).get_data()
        elif r >= 9:
            # load mask
            mask_data = nib.load(datadir + subjs[s] + '/' + subjs[s] + task_fn + str(r+1) + mask_fn_suffix).get_data()

        custom_mask = custom_mask + mask_data

custom_mask[custom_mask != numSubjsRuns] = 0
custom_mask[custom_mask == numSubjsRuns] = 1

maxval = np.max(custom_mask)
minval = np.min(custom_mask)
img = nib.Nifti1Image(custom_mask, affine=mni_brain.affine)
img.header['cal_min'] = minval
img.header['cal_max'] = maxval

nib.save(img,'/tigress/epiazza/keyboard/rois/custom_mask.nii.gz')
