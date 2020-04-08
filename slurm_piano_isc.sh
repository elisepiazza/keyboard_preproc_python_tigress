#!/bin/bash

#name job pythondemo, output to slurm file, use partition all, run for 1500 minutes and use 40GB of ram
#SBATCH -J 'piano_isc'
#SBATCH -o logfiles/piano_isc-%j.out
#SBATCH --error=logfiles/piano_isc%j.err
#SBATCH -p all
#SBATCH -t 500
#SBATCH -c 3 --mem 5000
#SBATCH --mail-type ALL
#SBATCH --mail-user epiazza@princeton.edu

module load pyger
export PYTHONMALLOC=debug

python -duv /tigress/epiazza/keyboard/scripts/piano_isc.py
