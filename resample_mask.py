import numpy as np
import nibabel as nib
from nilearn.image import resample_img
import nilearn.masking

# load custom mask
custom_mask = nib.load('/tigress/epiazza/keyboard/rois/custom_mask.nii.gz')

# load data to be resampled
input_data = nib.load('/tigress/epiazza/keyboard/rois/a1plus_2mm.nii.gz')

img_in_mm_space = resample_img(input_data, target_affine=custom_mask.affine,
                               target_shape=(65, 77, 65))

# binarize mask
mask_no_bin = img_in_mm_space.get_data().flatten()
mask_no_bin[mask_no_bin < 1] = 0
mask_bin = np.reshape(mask_no_bin, (65, 77, 65))

# save mask
maxval = np.max(mask_bin)
minval = np.min(mask_bin)
img = nib.Nifti1Image(mask_bin, affine=custom_mask.affine)
img.header['cal_min'] = minval
img.header['cal_max'] = maxval

# find intersection of custom mask and resampled mask
mask_lst = [custom_mask, img]
custom_resampled_msk = nilearn.masking.intersect_masks(mask_lst,threshold=1)

nib.save(custom_resampled_msk, '/tigress/epiazza/keyboard/rois/a1plus_3mm_custom.nii.gz')

