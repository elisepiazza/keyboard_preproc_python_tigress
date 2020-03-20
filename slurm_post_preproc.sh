#!/bin/bash

#name job pythondemo, output to slurm file, use partition all, run for 1500 minutes and use 40GB of ram
#SBATCH -J 'preproc_data'
#SBATCH -o logfiles/preproc_data-%j.out
#SBATCH --error=logfiles/preproc_data%j.err
#SBATCH -p all
#SBATCH -t 1000
#SBATCH -c 5 --mem 1000
#SBATCH --mail-type ALL
#SBATCH --mail-user epiazza@princeton.edu
#SBATCH --array=0-5

module load pyger
export PYTHONMALLOC=debug

python -duv /tigress/epiazza/keyboard/scripts/piano_post_preproc.py $SLURM_ARRAY_TASK_ID
