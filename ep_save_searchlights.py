import numpy as np
import sys
import nibabel as nib
from scipy.spatial import distance

subjs = ['sub-103','sub-105','sub-117','sub-120','sub-121']

keyboard_fn = ['_clean_data_run1.nii.gz','_clean_data_run2.nii.gz', '_clean_data_run3.nii.gz', '_clean_data_run4.nii.gz', '_clean_data_run5.nii.gz', 
'_clean_data_run6.nii.gz', '_clean_data_run7.nii.gz', '_clean_data_run8.nii.gz', '_clean_data_run9.nii.gz', '_clean_data_run10.nii.gz', 
'_clean_data_run11.nii.gz', '_clean_data_run12.nii.gz', '_clean_data_run13.nii.gz', '_clean_data_run14.nii.gz', '_clean_data_run15.nii.gz', 
'_clean_data_run16.nii.gz', '_clean_data_run17.nii.gz', '_clean_data_run18.nii.gz']

keyboard_brain_masks = ['_ses-01_task-keyboard_run-01_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz', '_ses-01_task-keyboard_run-02_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz', 
'_ses-01_task-keyboard_run-03_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz', '_ses-01_task-keyboard_run-04_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz',
'_ses-01_task-keyboard_run-05_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz', '_ses-01_task-keyboard_run-06_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz',
'_ses-01_task-keyboard_run-07_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz', '_ses-01_task-keyboard_run-08_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz',
'_ses-01_task-keyboard_run-09_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz', '_ses-01_task-keyboard_run-10_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz',
'_ses-01_task-keyboard_run-11_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz', '_ses-01_task-keyboard_run-12_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz',
'_ses-01_task-keyboard_run-13_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz', '_ses-01_task-keyboard_run-14_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz',
'_ses-01_task-keyboard_run-15_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz', '_ses-01_task-keyboard_run-16_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz',
'_ses-01_task-keyboard_run-17_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz', '_ses-01_task-keyboard_run-18_space-MNI152NLin2009cAsym_desc-brain_mask.nii.gz']

s = int(sys.argv[1])

datadir = '/tigress/epiazza/keyboard/data/'

# load subj data for each run separately
run1 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_fn[0]).get_data()
run2 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_fn[1]).get_data()
run3 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_fn[2]).get_data()
run4 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_fn[3]).get_data()
run5 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_fn[4]).get_data()
run6 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_fn[5]).get_data()
run7 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_fn[6]).get_data()
run8 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_fn[7]).get_data()
run9 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_fn[8]).get_data()
run10 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_fn[9]).get_data()
run11 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_fn[10]).get_data()
run12 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_fn[11]).get_data()
run13 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_fn[12]).get_data()
run14 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_fn[13]).get_data()
run15 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_fn[14]).get_data()
run16 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_fn[15]).get_data()
run17 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_fn[16]).get_data()
run18 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_fn[17]).get_data()


mask_run1 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_brain_masks[0]).get_data()
mask_run2 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_brain_masks[1]).get_data()
mask_run3 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_brain_masks[2]).get_data()
mask_run4 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_brain_masks[3]).get_data()
mask_run5 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_brain_masks[4]).get_data()
mask_run6 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_brain_masks[5]).get_data()
mask_run7 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_brain_masks[6]).get_data()
mask_run8 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_brain_masks[7]).get_data()
mask_run9 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_brain_masks[8]).get_data()
mask_run10 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_brain_masks[9]).get_data()
mask_run11 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_brain_masks[10]).get_data()
mask_run12 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_brain_masks[11]).get_data()
mask_run13 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_brain_masks[12]).get_data()
mask_run14 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_brain_masks[13]).get_data()
mask_run15 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_brain_masks[14]).get_data()
mask_run16 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_brain_masks[15]).get_data()
mask_run17 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_brain_masks[16]).get_data()
mask_run18 = nib.load(datadir + subjs[s] + '/' + subjs[s] + keyboard_brain_masks[17]).get_data()


print('Data Loaded')

# reshape mask data
mask_run1_reshape = np.reshape(mask_run1,(78*93*78))
mask_run2_reshape = np.reshape(mask_run2,(78*93*78))

# set searchlight parameters
stride = 5
radius = 5
min_vox = 10
 


x,y,z = np.mgrid[[slice(dm) for dm in run1.shape[0:3]]] 
x = np.reshape(x,(x.shape[0]*x.shape[1]*x.shape[2]))
y = np.reshape(y,(y.shape[0]*y.shape[1]*y.shape[2]))
z = np.reshape(z,(z.shape[0]*z.shape[1]*z.shape[2]))

# save searchlight input data for each coordinate for run 1 playing
coords1 = np.vstack((x,y,z)).T
coords1 = coords1[mask_run1_reshape>0]
for x in range(0,np.max(coords1, axis=0)[0]+stride,stride):
    for y in range(0,np.max(coords1, axis=0)[1]+stride,stride):
       for z in range(0,np.max(coords1, axis=0)[2]+stride,stride):
          D = distance.cdist(coords1,np.array([x,y,z]).reshape((1,3)))[:,0]
          SL_vox = D <= radius
          if np.sum(SL_vox) < min_vox:
             continue
          SL_mask = np.zeros(run1.shape[:-1],dtype=bool)
          SL_mask[mask_run1 > 0] = SL_vox
          sl_run1 = run1[SL_mask]
          np.save(datadir + subjs[s] + '/searchlight_input/run1/' + str(x)+'_'+str(y)+'_'+str(z),sl_run1)



x,y,z = np.mgrid[[slice(dm) for dm in run2.shape[0:3]]] 
x = np.reshape(x,(x.shape[0]*x.shape[1]*x.shape[2]))
y = np.reshape(y,(y.shape[0]*y.shape[1]*y.shape[2]))
z = np.reshape(z,(z.shape[0]*z.shape[1]*z.shape[2]))
     
# save searchlight input data for each coordinate for run 2 playing
coords2 = np.vstack((x,y,z)).T
coords2 = coords2[mask_run2_reshape>0]
for x in range(0,np.max(coords2, axis=0)[0]+stride,stride):
    for y in range(0,np.max(coords2, axis=0)[1]+stride,stride):
       for z in range(0,np.max(coords2, axis=0)[2]+stride,stride):
          D = distance.cdist(coords2,np.array([x,y,z]).reshape((1,3)))[:,0]
          SL_vox = D <= radius
          if np.sum(SL_vox) < min_vox:
             continue
          SL_mask = np.zeros(run2.shape[:-1],dtype=bool)
          SL_mask[mask_run2 > 0] = SL_vox
          sl_run2 = run2[SL_mask]
          np.save(datadir + subjs[s] + '/searchlight_input/run2/' + str(x)+'_'+str(y)+'_'+str(z),sl_run2)  



x,y,z = np.mgrid[[slice(dm) for dm in run3.shape[0:3]]] 
x = np.reshape(x,(x.shape[0]*x.shape[1]*x.shape[2]))
y = np.reshape(y,(y.shape[0]*y.shape[1]*y.shape[2]))
z = np.reshape(z,(z.shape[0]*z.shape[1]*z.shape[2]))
     
# save searchlight input data for each coordinate for run 3 playing
coords3 = np.vstack((x,y,z)).T
coords3 = coords3[mask_run3_reshape>0]
for x in range(0,np.max(coords3, axis=0)[0]+stride,stride):
    for y in range(0,np.max(coords3, axis=0)[1]+stride,stride):
       for z in range(0,np.max(coords3, axis=0)[2]+stride,stride):
          D = distance.cdist(coords3,np.array([x,y,z]).reshape((1,3)))[:,0]
          SL_vox = D <= radius
          if np.sum(SL_vox) < min_vox:
             continue
          SL_mask = np.zeros(run3.shape[:-1],dtype=bool)
          SL_mask[mask_run3 > 0] = SL_vox
          sl_run3 = run3[SL_mask]
          np.save(datadir + subjs[s] + '/searchlight_input/run3/' + str(x)+'_'+str(y)+'_'+str(z),sl_run3)  


x,y,z = np.mgrid[[slice(dm) for dm in run4.shape[0:3]]] 
x = np.reshape(x,(x.shape[0]*x.shape[1]*x.shape[2]))
y = np.reshape(y,(y.shape[0]*y.shape[1]*y.shape[2]))
z = np.reshape(z,(z.shape[0]*z.shape[1]*z.shape[2]))
     
# save searchlight input data for each coordinate for run 4 playing
coords4 = np.vstack((x,y,z)).T
coords4 = coords4[mask_run4_reshape>0]
for x in range(0,np.max(coords4, axis=0)[0]+stride,stride):
    for y in range(0,np.max(coords4, axis=0)[1]+stride,stride):
       for z in range(0,np.max(coords4, axis=0)[2]+stride,stride):
          D = distance.cdist(coords4,np.array([x,y,z]).reshape((1,3)))[:,0]
          SL_vox = D <= radius
          if np.sum(SL_vox) < min_vox:
             continue
          SL_mask = np.zeros(run4.shape[:-1],dtype=bool)
          SL_mask[mask_run4 > 0] = SL_vox
          sl_run4 = run4[SL_mask]
          np.save(datadir + subjs[s] + '/searchlight_input/run4/' + str(x)+'_'+str(y)+'_'+str(z),sl_run4)  


x,y,z = np.mgrid[[slice(dm) for dm in run5.shape[0:3]]] 
x = np.reshape(x,(x.shape[0]*x.shape[1]*x.shape[2]))
y = np.reshape(y,(y.shape[0]*y.shape[1]*y.shape[2]))
z = np.reshape(z,(z.shape[0]*z.shape[1]*z.shape[2]))
     
# save searchlight input data for each coordinate for run 5 playing
coords5 = np.vstack((x,y,z)).T
coords5 = coords5[mask_run5_reshape>0]
for x in range(0,np.max(coords5, axis=0)[0]+stride,stride):
    for y in range(0,np.max(coords5, axis=0)[1]+stride,stride):
       for z in range(0,np.max(coords5, axis=0)[2]+stride,stride):
          D = distance.cdist(coords5,np.array([x,y,z]).reshape((1,3)))[:,0]
          SL_vox = D <= radius
          if np.sum(SL_vox) < min_vox:
             continue
          SL_mask = np.zeros(run5.shape[:-1],dtype=bool)
          SL_mask[mask_run5 > 0] = SL_vox
          sl_run5 = run5[SL_mask]
          np.save(datadir + subjs[s] + '/searchlight_input/run5/' + str(x)+'_'+str(y)+'_'+str(z),sl_run5) 


x,y,z = np.mgrid[[slice(dm) for dm in run6.shape[0:3]]] 
x = np.reshape(x,(x.shape[0]*x.shape[1]*x.shape[2]))
y = np.reshape(y,(y.shape[0]*y.shape[1]*y.shape[2]))
z = np.reshape(z,(z.shape[0]*z.shape[1]*z.shape[2]))
     
# save searchlight input data for each coordinate for run 6 playing
coords6 = np.vstack((x,y,z)).T
coords6 = coords6[mask_run6_reshape>0]
for x in range(0,np.max(coords6, axis=0)[0]+stride,stride):
    for y in range(0,np.max(coords6, axis=0)[1]+stride,stride):
       for z in range(0,np.max(coords6, axis=0)[2]+stride,stride):
          D = distance.cdist(coords6,np.array([x,y,z]).reshape((1,3)))[:,0]
          SL_vox = D <= radius
          if np.sum(SL_vox) < min_vox:
             continue
          SL_mask = np.zeros(run6.shape[:-1],dtype=bool)
          SL_mask[mask_run6 > 0] = SL_vox
          sl_run6 = run6[SL_mask]
          np.save(datadir + subjs[s] + '/searchlight_input/run6/' + str(x)+'_'+str(y)+'_'+str(z),sl_run6) 



x,y,z = np.mgrid[[slice(dm) for dm in run7.shape[0:3]]] 
x = np.reshape(x,(x.shape[0]*x.shape[1]*x.shape[2]))
y = np.reshape(y,(y.shape[0]*y.shape[1]*y.shape[2]))
z = np.reshape(z,(z.shape[0]*z.shape[1]*z.shape[2]))
     
# save searchlight input data for each coordinate for run 7 playing
coords7 = np.vstack((x,y,z)).T
coords7 = coords7[mask_run7_reshape>0]
for x in range(0,np.max(coords7, axis=0)[0]+stride,stride):
    for y in range(0,np.max(coords7, axis=0)[1]+stride,stride):
       for z in range(0,np.max(coords7, axis=0)[2]+stride,stride):
          D = distance.cdist(coords7,np.array([x,y,z]).reshape((1,3)))[:,0]
          SL_vox = D <= radius
          if np.sum(SL_vox) < min_vox:
             continue
          SL_mask = np.zeros(run7.shape[:-1],dtype=bool)
          SL_mask[mask_run7 > 0] = SL_vox
          sl_run7 = run7[SL_mask]
          np.save(datadir + subjs[s] + '/searchlight_input/run7/' + str(x)+'_'+str(y)+'_'+str(z),sl_run7) 


x,y,z = np.mgrid[[slice(dm) for dm in run8.shape[0:3]]] 
x = np.reshape(x,(x.shape[0]*x.shape[1]*x.shape[2]))
y = np.reshape(y,(y.shape[0]*y.shape[1]*y.shape[2]))
z = np.reshape(z,(z.shape[0]*z.shape[1]*z.shape[2]))
     
# save searchlight input data for each coordinate for run 8 playing
coords8 = np.vstack((x,y,z)).T
coords8 = coords8[mask_run8_reshape>0]
for x in range(0,np.max(coords8, axis=0)[0]+stride,stride):
    for y in range(0,np.max(coords8, axis=0)[1]+stride,stride):
       for z in range(0,np.max(coords8, axis=0)[2]+stride,stride):
          D = distance.cdist(coords8,np.array([x,y,z]).reshape((1,3)))[:,0]
          SL_vox = D <= radius
          if np.sum(SL_vox) < min_vox:
             continue
          SL_mask = np.zeros(run8.shape[:-1],dtype=bool)
          SL_mask[mask_run8 > 0] = SL_vox
          sl_run8 = run8[SL_mask]
          np.save(datadir + subjs[s] + '/searchlight_input/run8/' + str(x)+'_'+str(y)+'_'+str(z),sl_run8) 



x,y,z = np.mgrid[[slice(dm) for dm in run9.shape[0:3]]] 
x = np.reshape(x,(x.shape[0]*x.shape[1]*x.shape[2]))
y = np.reshape(y,(y.shape[0]*y.shape[1]*y.shape[2]))
z = np.reshape(z,(z.shape[0]*z.shape[1]*z.shape[2]))
     
# save searchlight input data for each coordinate for run 9 playing
coords9 = np.vstack((x,y,z)).T
coords9 = coords9[mask_run9_reshape>0]
for x in range(0,np.max(coords9, axis=0)[0]+stride,stride):
    for y in range(0,np.max(coords9, axis=0)[1]+stride,stride):
       for z in range(0,np.max(coords9, axis=0)[2]+stride,stride):
          D = distance.cdist(coords9,np.array([x,y,z]).reshape((1,3)))[:,0]
          SL_vox = D <= radius
          if np.sum(SL_vox) < min_vox:
             continue
          SL_mask = np.zeros(run9.shape[:-1],dtype=bool)
          SL_mask[mask_run9 > 0] = SL_vox
          sl_run9 = run9[SL_mask]
          np.save(datadir + subjs[s] + '/searchlight_input/run9/' + str(x)+'_'+str(y)+'_'+str(z),sl_run9) 


x,y,z = np.mgrid[[slice(dm) for dm in run10.shape[0:3]]] 
x = np.reshape(x,(x.shape[0]*x.shape[1]*x.shape[2]))
y = np.reshape(y,(y.shape[0]*y.shape[1]*y.shape[2]))
z = np.reshape(z,(z.shape[0]*z.shape[1]*z.shape[2]))
     
# save searchlight input data for each coordinate for run 10 playing
coords10 = np.vstack((x,y,z)).T
coords10 = coords10[mask_run10_reshape>0]
for x in range(0,np.max(coords10, axis=0)[0]+stride,stride):
    for y in range(0,np.max(coords10, axis=0)[1]+stride,stride):
       for z in range(0,np.max(coords10, axis=0)[2]+stride,stride):
          D = distance.cdist(coords10,np.array([x,y,z]).reshape((1,3)))[:,0]
          SL_vox = D <= radius
          if np.sum(SL_vox) < min_vox:
             continue
          SL_mask = np.zeros(run10.shape[:-1],dtype=bool)
          SL_mask[mask_run10 > 0] = SL_vox
          sl_run10 = run10[SL_mask]
          np.save(datadir + subjs[s] + '/searchlight_input/run10/' + str(x)+'_'+str(y)+'_'+str(z),sl_run10)


x,y,z = np.mgrid[[slice(dm) for dm in run11.shape[0:3]]] 
x = np.reshape(x,(x.shape[0]*x.shape[1]*x.shape[2]))
y = np.reshape(y,(y.shape[0]*y.shape[1]*y.shape[2]))
z = np.reshape(z,(z.shape[0]*z.shape[1]*z.shape[2]))
     
# save searchlight input data for each coordinate for run 11 playing
coords11 = np.vstack((x,y,z)).T
coords11 = coords11[mask_run11_reshape>0]
for x in range(0,np.max(coords11, axis=0)[0]+stride,stride):
    for y in range(0,np.max(coords11, axis=0)[1]+stride,stride):
       for z in range(0,np.max(coords11, axis=0)[2]+stride,stride):
          D = distance.cdist(coords11,np.array([x,y,z]).reshape((1,3)))[:,0]
          SL_vox = D <= radius
          if np.sum(SL_vox) < min_vox:
             continue
          SL_mask = np.zeros(run11.shape[:-1],dtype=bool)
          SL_mask[mask_run11 > 0] = SL_vox
          sl_run11 = run11[SL_mask]
          np.save(datadir + subjs[s] + '/searchlight_input/run11/' + str(x)+'_'+str(y)+'_'+str(z),sl_run11)          


x,y,z = np.mgrid[[slice(dm) for dm in run12.shape[0:3]]] 
x = np.reshape(x,(x.shape[0]*x.shape[1]*x.shape[2]))
y = np.reshape(y,(y.shape[0]*y.shape[1]*y.shape[2]))
z = np.reshape(z,(z.shape[0]*z.shape[1]*z.shape[2]))
     
# save searchlight input data for each coordinate for run 12 playing
coords12 = np.vstack((x,y,z)).T
coords12 = coords12[mask_run12_reshape>0]
for x in range(0,np.max(coords12, axis=0)[0]+stride,stride):
    for y in range(0,np.max(coords12, axis=0)[1]+stride,stride):
       for z in range(0,np.max(coords12, axis=0)[2]+stride,stride):
          D = distance.cdist(coords12,np.array([x,y,z]).reshape((1,3)))[:,0]
          SL_vox = D <= radius
          if np.sum(SL_vox) < min_vox:
             continue
          SL_mask = np.zeros(run12.shape[:-1],dtype=bool)
          SL_mask[mask_run12 > 0] = SL_vox
          sl_run12 = run12[SL_mask]
          np.save(datadir + subjs[s] + '/searchlight_input/run12/' + str(x)+'_'+str(y)+'_'+str(z),sl_run12) 


x,y,z = np.mgrid[[slice(dm) for dm in run13.shape[0:3]]] 
x = np.reshape(x,(x.shape[0]*x.shape[1]*x.shape[2]))
y = np.reshape(y,(y.shape[0]*y.shape[1]*y.shape[2]))
z = np.reshape(z,(z.shape[0]*z.shape[1]*z.shape[2]))
     
# save searchlight input data for each coordinate for run 13 playing
coords13 = np.vstack((x,y,z)).T
coords13 = coords13[mask_run13_reshape>0]
for x in range(0,np.max(coords13, axis=0)[0]+stride,stride):
    for y in range(0,np.max(coords13, axis=0)[1]+stride,stride):
       for z in range(0,np.max(coords13, axis=0)[2]+stride,stride):
          D = distance.cdist(coords13,np.array([x,y,z]).reshape((1,3)))[:,0]
          SL_vox = D <= radius
          if np.sum(SL_vox) < min_vox:
             continue
          SL_mask = np.zeros(run13.shape[:-1],dtype=bool)
          SL_mask[mask_run13 > 0] = SL_vox
          sl_run13 = run13[SL_mask]
          np.save(datadir + subjs[s] + '/searchlight_input/run13/' + str(x)+'_'+str(y)+'_'+str(z),sl_run13)  


x,y,z = np.mgrid[[slice(dm) for dm in run14.shape[0:3]]] 
x = np.reshape(x,(x.shape[0]*x.shape[1]*x.shape[2]))
y = np.reshape(y,(y.shape[0]*y.shape[1]*y.shape[2]))
z = np.reshape(z,(z.shape[0]*z.shape[1]*z.shape[2]))
     
# save searchlight input data for each coordinate for run 14 playing
coords14 = np.vstack((x,y,z)).T
coords14 = coords14[mask_run14_reshape>0]
for x in range(0,np.max(coords14, axis=0)[0]+stride,stride):
    for y in range(0,np.max(coords14, axis=0)[1]+stride,stride):
       for z in range(0,np.max(coords14, axis=0)[2]+stride,stride):
          D = distance.cdist(coords14,np.array([x,y,z]).reshape((1,3)))[:,0]
          SL_vox = D <= radius
          if np.sum(SL_vox) < min_vox:
             continue
          SL_mask = np.zeros(run14.shape[:-1],dtype=bool)
          SL_mask[mask_run14 > 0] = SL_vox
          sl_run14 = run14[SL_mask]
          np.save(datadir + subjs[s] + '/searchlight_input/run14/' + str(x)+'_'+str(y)+'_'+str(z),sl_run14) 


x,y,z = np.mgrid[[slice(dm) for dm in run15.shape[0:3]]] 
x = np.reshape(x,(x.shape[0]*x.shape[1]*x.shape[2]))
y = np.reshape(y,(y.shape[0]*y.shape[1]*y.shape[2]))
z = np.reshape(z,(z.shape[0]*z.shape[1]*z.shape[2]))
     
# save searchlight input data for each coordinate for run 15 playing
coords15 = np.vstack((x,y,z)).T
coords15 = coords15[mask_run15_reshape>0]
for x in range(0,np.max(coords15, axis=0)[0]+stride,stride):
    for y in range(0,np.max(coords15, axis=0)[1]+stride,stride):
       for z in range(0,np.max(coords15, axis=0)[2]+stride,stride):
          D = distance.cdist(coords15,np.array([x,y,z]).reshape((1,3)))[:,0]
          SL_vox = D <= radius
          if np.sum(SL_vox) < min_vox:
             continue
          SL_mask = np.zeros(run15.shape[:-1],dtype=bool)
          SL_mask[mask_run15 > 0] = SL_vox
          sl_run15 = run15[SL_mask]
          np.save(datadir + subjs[s] + '/searchlight_input/run15/' + str(x)+'_'+str(y)+'_'+str(z),sl_run15)   


x,y,z = np.mgrid[[slice(dm) for dm in run16.shape[0:3]]] 
x = np.reshape(x,(x.shape[0]*x.shape[1]*x.shape[2]))
y = np.reshape(y,(y.shape[0]*y.shape[1]*y.shape[2]))
z = np.reshape(z,(z.shape[0]*z.shape[1]*z.shape[2]))
     
# save searchlight input data for each coordinate for run 16 playing
coords16 = np.vstack((x,y,z)).T
coords16 = coords16[mask_run16_reshape>0]
for x in range(0,np.max(coords16, axis=0)[0]+stride,stride):
    for y in range(0,np.max(coords16, axis=0)[1]+stride,stride):
       for z in range(0,np.max(coords16, axis=0)[2]+stride,stride):
          D = distance.cdist(coords16,np.array([x,y,z]).reshape((1,3)))[:,0]
          SL_vox = D <= radius
          if np.sum(SL_vox) < min_vox:
             continue
          SL_mask = np.zeros(run16.shape[:-1],dtype=bool)
          SL_mask[mask_run16 > 0] = SL_vox
          sl_run16 = run16[SL_mask]
          np.save(datadir + subjs[s] + '/searchlight_input/run16/' + str(x)+'_'+str(y)+'_'+str(z),sl_run16)  


x,y,z = np.mgrid[[slice(dm) for dm in run17.shape[0:3]]] 
x = np.reshape(x,(x.shape[0]*x.shape[1]*x.shape[2]))
y = np.reshape(y,(y.shape[0]*y.shape[1]*y.shape[2]))
z = np.reshape(z,(z.shape[0]*z.shape[1]*z.shape[2]))
     
# save searchlight input data for each coordinate for run 17 playing
coords17 = np.vstack((x,y,z)).T
coords17 = coords17[mask_run17_reshape>0]
for x in range(0,np.max(coords17, axis=0)[0]+stride,stride):
    for y in range(0,np.max(coords17, axis=0)[1]+stride,stride):
       for z in range(0,np.max(coords17, axis=0)[2]+stride,stride):
          D = distance.cdist(coords17,np.array([x,y,z]).reshape((1,3)))[:,0]
          SL_vox = D <= radius
          if np.sum(SL_vox) < min_vox:
             continue
          SL_mask = np.zeros(run17.shape[:-1],dtype=bool)
          SL_mask[mask_run17 > 0] = SL_vox
          sl_run17 = run17[SL_mask]
          np.save(datadir + subjs[s] + '/searchlight_input/run17/' + str(x)+'_'+str(y)+'_'+str(z),sl_run17)    


x,y,z = np.mgrid[[slice(dm) for dm in run18.shape[0:3]]] 
x = np.reshape(x,(x.shape[0]*x.shape[1]*x.shape[2]))
y = np.reshape(y,(y.shape[0]*y.shape[1]*y.shape[2]))
z = np.reshape(z,(z.shape[0]*z.shape[1]*z.shape[2]))
     
# save searchlight input data for each coordinate for run 18 playing
coords18 = np.vstack((x,y,z)).T
coords18 = coords18[mask_run18_reshape>0]
for x in range(0,np.max(coords18, axis=0)[0]+stride,stride):
    for y in range(0,np.max(coords18, axis=0)[1]+stride,stride):
       for z in range(0,np.max(coords18, axis=0)[2]+stride,stride):
          D = distance.cdist(coords18,np.array([x,y,z]).reshape((1,3)))[:,0]
          SL_vox = D <= radius
          if np.sum(SL_vox) < min_vox:
             continue
          SL_mask = np.zeros(run18.shape[:-1],dtype=bool)
          SL_mask[mask_run18 > 0] = SL_vox
          sl_run18 = run18[SL_mask]
          np.save(datadir + subjs[s] + '/searchlight_input/run18/' + str(x)+'_'+str(y)+'_'+str(z),sl_run18)  
