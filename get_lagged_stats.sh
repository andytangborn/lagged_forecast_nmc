#!/bin/bash
#SBATCH -J get_lagged_stats  
#SBATCH -A da-cpu
#SBATCH --open-mode=truncate
#SBATCH -o log.bumpaero
#SBATCH -e log.bumpaero
#SBATCH --nodes=10
#SBATCH -q batch 
#SBATCH -t 0:20:00


emcpy_mod

python get_lagged_stats.py  



