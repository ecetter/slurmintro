#!/bin/bash

#SBATCH --job-name=pyfibotri        		#### give the job a name
#SBATCH --account=open             		#### specify the account
#SBATCH --partition=open           		#### specify the partition
#SBATCH --nodes=1                  		#### request a node
#SBATCH --ntasks=1                 		#### request a task / cpu
#SBATCH --mem=4G                   		#### request the memory required per node
#SBATCH --time=00:10:00            		#### set a limit on the total run time

echo "Job ID is $SLURM_JOB_ID."
echo "Executing on the machine: " $(hostname)

time python3 fibonacci_triangle.py 25 > fibonacci_triangle.out
