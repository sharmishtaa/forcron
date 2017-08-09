import paramiko
import os
import time


#incronfnames = ["/pipeline/incron/pipeline/nas2/acq_cron","/pipeline/incron/pipeline/nas2/acq_cron","/pipeline/incron/pipeline/nas3/acq_cron","/pipeline/incron/pipeline/nas4/acq_cron"]
incronfnames = ["/pipeline/incron/pipeline/nas2/acq_cron"]

#incronfnames = ["/pipeline/incron/pipeline/nas/acq_cron"]
index = 0


for i in range (0,2):

	with open("/pipeline/forcron/confirm_data2process") as f:
		alldirnames = f.readlines()

	for dirname in alldirnames:
		for sectnum in range(0,65):
			outputstring = "%s,%d,M246930_Scnn1a"%(dirname.strip(),sectnum)
			print outputstring
			fname = incronfnames[index]
			cmd = "echo %s > %s "%(outputstring,fname)
			print fname
			os.system(cmd)

			runcmd = "python /pipeline/forcron/runme_acquisition2.py"
			os.system(runcmd)

			index = index+1
			if (index > 0):
				index = 0
			time.sleep(120)
			
			
	



