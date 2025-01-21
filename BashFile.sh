#!/bin/bash

#SBATCH --job-name=texts
#SBATCH --time=0-23:30:00
#SBATCH --nodes=1
#SBATCH --tasks=1
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --exclude=gpu-node[001-004]
#SBATCH --output=output.log
#SBATCH --error=error.log

module load GpuModules
module load pytorch-py37-cuda11.2-gcc8/1.9.1

# Initialize Conda (adjust the path if necessary)
source /home/g063292/miniconda3/etc/profile.d/conda.sh

# Activate your Conda environment
conda activate TextS

# Run your script
srun python main.py
# python3 "$PYTHON_SCRIPT"
# --mpi=pmi2
# CSBATCH --nodelist=gpu-node004'
# CSBATCH --exclude=gpu-node[001-004]
