import os
import time
import sys
sys.path.insert(0,'/data/array_tomography/ForSharmi/allen_SB_code/celery/')
from celery import Celery
from tasks import run_celerycommand

project_dir = "/nas4/data/S3_Run1_Jarvis"

firstribbon = 68
lastribbon = 113

for i in range(firstribbon,lastribbon):
	cmd = "python /data/array_tomography/ForSharmi/allen_SB_code/MakeAT/make_median.py "
	cmd = cmd+ "--inputDirectory /nas4/data/S3_Run1_Jarvis/raw/data/Ribbon%04d/session01/Gephyrin/ --filepart Gephyrin --outputImage /nas4/data/S3_Run1_Jarvis/processed/median1/Median_Gephyrin_Ribbon%04d.tif"%(i,i)
	print cmd
	result = run_celerycommand.apply_async(args=[cmd,os.getcwd()])
	if i%5 == 0:
		time.sleep(60)
		
