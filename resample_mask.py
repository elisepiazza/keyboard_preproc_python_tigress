import numpy as np
import nibabel as nib
from nilearn.image import resample_img

# load output affine matrix
output_affine = nib.load('/tigress/epiazza/keyboard/rois/MNI152_T1_3mm_brain.nii.gz').affine

# load data to be resampled
input_data = nib.load('/tigress/epiazza/keyboard/rois/vmPFC_mask.nii.gz')

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
nib.save(img, '/tigress/epiazza/keyboard/rois/vmPFC_mask_3mm.nii.gz')


