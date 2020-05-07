import numpy as np
import sys
import nibabel as nib
from scipy.spatial import distance
import os

subjs = ['sub-103', 'sub-105', 'sub-108', 'sub-115', 'sub-117', 'sub-120', 'sub-121', 'sub-122', 'sub-123']

s = int(sys.argv[1])

nRuns = 18

datadir = '/tigress/epiazza/keyboard/data/'

# set searchlight parameters
stride = 5
radius = 5
min_vox = 10

mask = nib.load('/tigress/epiazza/keyboard/rois/custom_mask.nii.gz').get_data()

# reshape mask data
mask_reshape = np.reshape(mask,(65*77*65))

for i in range(nRuns):
    # load each run into list
    run = nib.load(datadir + subjs[s] + '/clean_data/clean_data_run' + str(i+1) + '.nii.gz').get_data()
    print('Data Loaded')
    
    ## create searchlight input run directory
    #os.mkdir(datadir + subjs[s] + '/searchlight_input/run' + str(i+1))
 
    x,y,z = np.mgrid[[slice(dm) for dm in run.shape[0:3]]] 
    x = np.reshape(x,(x.shape[0]*x.shape[1]*x.shape[2]))
    y = np.reshape(y,(y.shape[0]*y.shape[1]*y.shape[2]))
    z = np.reshape(z,(z.shape[0]*z.shape[1]*z.shape[2]))

    # save searchlight input data for each coordinate for run 1 playing
    coords = np.vstack((x,y,z)).T
    coords = coords[mask_reshape>0]
    for x in range(0,np.max(coords, axis=0)[0]+stride,stride):
        for y in range(0,np.max(coords, axis=0)[1]+stride,stride):
           for z in range(0,np.max(coords, axis=0)[2]+stride,stride):
              D = distance.cdist(coords,np.array([x,y,z]).reshape((1,3)))[:,0]
              SL_vox = D <= radius
              if np.sum(SL_vox) < min_vox:
                 continue
              SL_mask = np.zeros(run.shape[:-1],dtype=bool)
              SL_mask[mask > 0] = SL_vox
              sl_run = run[SL_mask]
              np.save(datadir + subjs[s] + '/searchlight_input/run' + str(i+1) + '/' + str(x)+'_'+str(y)+'_'+str(z),sl_run)

