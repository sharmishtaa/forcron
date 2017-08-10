#!/pipeline/anaconda/bin/python

import os
import sys
sys.path.insert(0,'/data/array_tomography/ForSharmi/allen_SB_code/celery/')
from celery import Celery
from tasks import run_celerycommand


if __name__ == '__main__':
	
	cmd = "python /pipeline/forcron/runme_acquisition4.py"
	result = run_celerycommand.apply_async(args=[cmd,os.getcwd()])
	
