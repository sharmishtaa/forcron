import os
import sys
sys.path.insert(0,'/data/array_tomography/ForSharmi/allen_SB_code/celery/')
from celery import Celery
from tasks import run_celerycommand
import time

for ribnum in range(29,30):
	
	for sec in range(4,5):
			
		for sessnum in range(3,4):
			
			print ribnum
			print sec
			print sessnum

			#scmd = "PYTHONPATH='' luigi registersessions --module register_across_sessions_render --workers 4 "
			#scmd = scmd + "--statetable /nas3/data/SC_MT22_IUE1_2_PlungeLowicryl/scripts/statetable_ribbon_%d_session_%d_section_%d "%(ribnum,sessnum,sec)
			#scmd = scmd + "--refsession 1 "
			#scmd = scmd + "--owner SC_MT_IUE1_2"
			#print scmd
			
			scmd = "PYTHONPATH='' luigi registersessions --module register_across_sessions_render --workers 4 "
			scmd = scmd + "--statetable /nas2/data/HumanIHCopt_rnd1_control/scripts/statetable_ribbon_%d_session_%d_section_%d "%(ribnum,sessnum,sec)
			scmd = scmd + "--refsession 1 "
			scmd = scmd + "--owner Human_IHC_opt"
			print scmd
			
									 

			fname = "/pipeline/forcron/commands/runme_register.sh"
			f = open(fname,"w")
			f.write(scmd)
			f.close()
			rcmd = "docker exec luigiscripts sh /pipeline/forcron/commands/runme_register.sh"
			print rcmd
			#result = run_celerycommand.apply_async(args=[rcmd,os.getcwd()])
			os.system(rcmd)

			time.sleep(1)
