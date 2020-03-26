#!/bin/bash

#name job pythondemo, output to slurm file, use partition all, run for 1500 minutes and use 40GB of ram
#SBATCH -J 'save_searchlights'
#SBATCH -o logfiles/save_searchlights-%j.out
#SBATCH --error=logfiles/save_searchlights%j.err
#SBATCH -p all
#SBATCH -t 4000
#SBATCH -c 10 --mem 50000
#SBATCH --mail-type ALL
#SBATCH --mail-user epiazza@princeton.edu
#SBATCH --array=0-1

module load pyger/0.9.1
export PYTHONMALLOC=debug

python -duv /tigress/epiazza/keyboard/scripts/ep_save_searchlights.py $SLURM_ARRAY_TASK_ID  
