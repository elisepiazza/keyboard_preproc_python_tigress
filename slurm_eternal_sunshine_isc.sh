#!/bin/bash

#name job pythondemo, output to slurm file, use partition all, run for 1500 minutes and use 40GB of ram
#SBATCH -J 'eternal_sunshine_isc'
#SBATCH -o logfiles/eternal_sunshine_isc-%j.out
#SBATCH --error=logfiles/eternal_sunshine_isc%j.err
#SBATCH -p all
#SBATCH -t 1000
#SBATCH -c 10 --mem 50000
#SBATCH --mail-type ALL
#SBATCH --mail-user jamalw@princeton.edu

module load pyger
export PYTHONMALLOC=debug

python -duv /jukebox/norman/jamalw/Eternal_Sunshine/scripts/eternal_sunshine_isc.py
