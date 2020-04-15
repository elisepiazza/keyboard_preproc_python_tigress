import numpy as np
import nibabel as nib
from nilearn.image import resample_img

piano_fn = '/jukebox/hasson/elise/fMRI/fmriprep/keyboard/data/bids/derivatives/fmriprep/sub-103/ses-01/func/sub-103_ses-01_task-keyboard_run-18_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz'

# load output affine matrix
output_affine = nib.load(piano_fn).affine

# load data to be resampled
input_data = nib.load('/jukebox/norman/jamalw/MES/data/MNI152_T1_2mm_brain.nii')

img_in_mm_space = resample_img(input_data, target_affine=output_affine,
                               target_shape=(65, 77, 65))

# binarize mask
mask_no_bin = img_in_mm_space.get_data().flatten()
mask_no_bin[mask_no_bin < 1] = 0
mask_bin = np.reshape(mask_no_bin, (65, 77, 65))

# save mask
maxval = np.max(mask_bin)
minval = np.min(mask_bin)
img = nib.Nifti1Image(mask_bin, affine=output_affine)
img.header['cal_min'] = minval
img.header['cal_max'] = maxval
nib.save(img, '/jukebox/norman/jamalw/Eternal_Sunshine/data/nifti/MNI152_T1_3mm_brain.nii.gz')


