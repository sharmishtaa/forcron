#!/pipeline/anaconda/bin/python

import time
import os
#import sys
#sys.path.insert(0,os.getcwd())
#from sys import argv
import pandas as pd

import sys
sys.path.insert(0,'/data/array_tomography/ForSharmi/allen_SB_code/celery/')
from celery import Celery
from tasks import run_celerycommand

def parseprojectroot(projectdirectory):
	print projectdirectory
	tok = projectdirectory.split("/")
	dataind = tok.index('data')
	return tok[dataind+1]

def parsefile(fname):

	with open(fname) as f:
		content = f.readlines()

	if len(content)>1:
		print "File is corrupted..."
	else:
		#parse line

		fullline = content[0]
		fullinetok = fullline.split(",")
		section = int(fullinetok[1])
		owner = str(fullinetok[2])
		#owner = "TESTEXPERIMENT"

		line = fullinetok[0]

		proj = line.split("raw")
		projectdirectory = proj[0]

		tok = line.split("/")
		ribbondir = tok[len(tok)-2]
		sessiondir = tok[len(tok)-1]
		ribbon = int(ribbondir[6:])
		session = int(sessiondir[7:])

		return [projectdirectory, ribbon, session, section, owner,fullline]
		
def get_channel_nums(statetablefile):
	df=pd.read_csv(statetablefile)
	uniq_ch=df.groupby(['ch']).groups.keys()
	return uniq_ch

if __name__ == '__main__':

	cmd0 = "echo This file has been updated! > /pipeline/incron/michelle/update "
	os.system(cmd0)


	info = parsefile('/pipeline/incron/michelle/acq_cron')
	
	projectdirectory = info[0]
	ribbon = info[1];
	session = info[2];
	section = info[3];
	owner = info[4];
	#owner = "TESTEXPERIMENT"

	projectname = parseprojectroot(projectdirectory)
	statetablefile =projectdirectory+ "/scripts/statetable_ribbon_%d_session_%d_section_%d"%(ribbon,session,section)

	#make state table
	cmd = "docker exec luigiscripts python make_state_table_ext_multi_pseudoz.py "
	cmd = cmd + "--projectDirectory %s "%projectdirectory
	cmd = cmd + "--outputFile  %s "%statetablefile
	cmd = cmd + "--oneribbononly True "
	cmd = cmd + "--ribbon %d "%ribbon
	cmd = cmd + "--session %d "%session
	cmd = cmd + "--section %d "%section
	print cmd
	os.system(cmd)
	print "......................................................."
	
	#run create_fast_stacks
	dcmd = "docker exec renderapps python append_fast_stacks.py "
	dcmd = dcmd + "--render.host ibs-forrestc-ux1 "
 	dcmd = dcmd + "--render.client_scripts /var/www/render/render-ws-java-client/src/main/scripts "
 	dcmd = dcmd + "--render.port 8080 "
 	dcmd = dcmd + "--render.memGB 5G "
 	dcmd = dcmd + "--log_level INFO "
	dcmd = dcmd + "--statetableFile %s "%statetablefile
	dcmd = dcmd + "--render.project %s "%projectname
 	dcmd = dcmd + "--projectDirectory %s "%projectdirectory
 	dcmd = dcmd + "--outputStackPrefix Acquisition "
	dcmd = dcmd + " --render.owner %s "%owner
 	print dcmd
	#os.system(dcmd)
	
	#run stitching
	allchans = get_channel_nums(statetablefile) 
	print allchans

	statetablefile = statetablefile.replace('//','/')
	
	for channelnum in allchans:
	#for channelnum in range (0,1):
		scmd = "PYTHONPATH='' luigi stitch_section --module stitching --workers 4 "
		scmd = scmd + "--statetablefile %s "%statetablefile
		scmd = scmd + "--ribbon %d "%ribbon
		scmd = scmd + "--section %d "%section
		scmd = scmd + "--session %d "%session
		scmd = scmd + "--channel %d "%channelnum
		scmd = scmd + "--owner %s"%owner
		print scmd
		
		tag = projectname + "_"+owner+"_"+statetablefile
		#waitcmd = "docker exec luigiscripts python /pipeline/luigi-scripts/wait_30_mins.py\n"
		fname = "/pipeline/forcron/commands/runme_stitchingm_%d%_%s.sh"%(channelnum,tag)
		f = open(fname,"w")
		#if channelnum > 0:
		#	f.write(waitcmd)
		f.write(scmd)
		f.close()
		
		rcmd = "docker exec luigiscripts sh /pipeline/forcron/commands/runme_stitchingm_%d_%s.sh"%(channelnum,tag)
		print rcmd
		os.system(rcmd)
		#result = run_celerycommand.apply_async(args=[rcmd,os.getcwd()])
	
		#time.sleep(10)
	
		




