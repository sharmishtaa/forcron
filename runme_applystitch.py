#!/pipeline/anaconda/bin/python

import time
import datetime as dt
from datetime import date,timedelta
import os
#import sys
#sys.path.insert(0,os.getcwd())
#from sys import argv
import argparse
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
	
def get_statetables_created_today(dir,prefix):
	fnames = []
	for root,dirs,files in os.walk(dir):
		for file_name in files:
			today = dt.date.today()
			path = os.path.join(root,file_name)
			st = os.stat(path)
			mod_date = dt.date.fromtimestamp(st.st_ctime)
			if mod_date == today:
				if file_name.startswith(prefix):
				#if file_name.startswith('statetable'):
					fnames.append(file_name)
					
	return fnames
	
def get_statetables_created_last3days(dir,prefix):
	fnames = []
	today = dt.date.today()
	yesterday = today - timedelta(1)
	daybefore = yesterday - timedelta(1)
	alldays = [today,yesterday,daybefore]
	
	for root,dirs,files in os.walk(dir):
		for file_name in files:
			
			path = os.path.join(root,file_name)
			st = os.stat(path)
			mod_date = dt.date.fromtimestamp(st.st_ctime)
			if mod_date in alldays:
				#if file_name.startswith('statetable'):
				if file_name.startswith(prefix):
					fnames.append(file_name)
					
	return fnames

def get_all_statetables(dir):
	fnames = []
	for root,dirs,files in os.walk(dir):
		for file_name in files:
			#today = dt.date.today()
			path = os.path.join(root,file_name)
			#st = os.stat(path)
			#mod_date = dt.date.fromtimestamp(st.st_ctime)
			#if mod_date == today:
			
			if file_name.startswith(prefix):
			#if file_name.startswith('statetable'):	
				fnames.append(file_name)

	return fnames
	
	
def parse_statetablename(s):
	#assumes name of form: statetable_ribbon_a_session_b_section_c and returns [a,b,c]
	tok = s.split('_')
	ribbon = int(tok[2])
	session = int(tok[4])
	section = int(tok[6])
	return [ribbon,session,section]
				

if __name__ == '__main__':
	
	parser = argparse.ArgumentParser(description="Run Apply stitching")
	parser.add_argument('--projectdirectory',nargs=1,help="projectdirectory")
	parser.add_argument('--owner',nargs=1,help="owner - meta experiment name")
	parser.add_argument('--processall',dest='processall',help="process all statetables",default=False,action='store_true')
	parser.add_argument('--processtoday',dest='processtoday',help="process todays statetables",default=False,action='store_true')
	parser.add_argument('--prefix',nargs=1,help="prefix of file name",default='statetable')
	args = parser.parse_args()
	

	projectdirectory = args.projectdirectory[0]
	owner = args.owner[0]
	statetabledirectory = os.path.join(projectdirectory, 'scripts')
	prefix = args.prefix[0]
	
	if args.processall == True:
		statetablefnames = get_all_statetables(statetabledirectory)
	elif args.processtoday == True:
		statetablefnames = get_statetables_created_today(statetabledirectory)
	else:
		statetablefnames = get_statetables_created_last3days(statetabledirectory)
	
	print statetablefnames
	


	
	for stf in statetablefnames: 
		
		[ribbon,session,section] = parse_statetablename(stf)
		projectname = parseprojectroot(projectdirectory)
		#statetablefile =projectdirectory+ "/scripts/statetable_ribbon_%d_session_%d_section_%d"%(ribbon,session,section)
		statetablefile =projectdirectory+ "/scripts/%s"%stf
		
		#run stitching
		allchans = get_channel_nums(statetablefile) 
		print allchans
		
		for channelnum in allchans:
		#for channelnum in range (2,3):
			
			scmd = "PYTHONPATH='' luigi stitch_section --module stitching --workers 4 "
			scmd = scmd + "--statetablefile %s "%statetablefile
			scmd = scmd + "--ribbon %d "%ribbon
			scmd = scmd + "--section %d "%section
			scmd = scmd + "--session %d "%session
			scmd = scmd + "--channel %d "%channelnum
			scmd = scmd + "--owner %s"%owner
			print scmd
			#exit(0)
			#waitcmd = "docker exec luigiscripts python /pipeline/luigi-scripts/wait_30_mins.py\n"
			fname = "/pipeline/forcron/commands/runme_applystitching_%d_%d_%d_%d.sh"%(ribbon,session,section,channelnum)
			f = open(fname,"w")
			#if channelnum > 0:
			#	f.write(waitcmd)
			f.write(scmd)
			f.close()
			
			rcmd = "docker exec luigiscripts sh /pipeline/forcron/commands/runme_applystitching_%d_%d_%d_%d.sh"%(ribbon,session,section,channelnum)
			print rcmd
			#os.system(rcmd)
			result = run_celerycommand.apply_async(args=[rcmd,os.getcwd()])
			
			#time.sleep(2)
			
		#time.sleep(30)
		
