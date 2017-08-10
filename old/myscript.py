import os
from sys import argv


def parseprojectroot(projectdirectory):
	
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
		line = content[0]
		
		proj = line.split("raw")
		projectdirectory = proj[0]
		
		tok = line.split("/")
		ribbondir = tok[len(tok)-2]
		sessiondir = tok[len(tok)-1]
		
		ribbon = int(ribbondir[6:])
		session = int(sessiondir[7:])
		
		return [projectdirectory, ribbon, session]

if __name__ == '__main__':

	#info = parsefile(argv[1])
	#info = parsefile('/nas4/job-scheduling/acq_cron')
	info = parsefile('/pipeline/incrontest/nas4/acq_cron')
	cmd = "echo hello > /home/sharmishtaas/triggeredoutput500"
	os.system(cmd)

	
	projectdirectory = info[0]
	ribbon = info[1];
	session = info[2];
	owner = "DryRun1_April_2017"
	projectname = parseprojectroot(projectdirectory)
	statetablefile =projectdirectory+ "/scripts/statetable_ribbon_%d_session_%d"%(ribbon,session)
	
	
	#make state table
	cmd = "docker exec luigiscripts python make_state_table_ext_multi_pseudoz.py "
	cmd = cmd + "--projectDirectory %s "%projectdirectory
	cmd = cmd + "--outputFile  %s "%statetablefile
	cmd = cmd + "--oneribbononly True "
	cmd = cmd + "--ribbon %d "%ribbon
	cmd = cmd + "--session %d "%session
	print cmd
	os.system(cmd)


	dcmd = "docker exec -t renderapps python append_fast_stacks.py "
	dcmd = dcmd + "--render.host ibs-forrestc-ux1 "
 	dcmd = dcmd + "--render.client_scripts /var/www/render/render-ws-java-client/src/main/scripts "
 	dcmd = dcmd + "--render.port 8080 "
 	dcmd = dcmd + "--render.memGB 5G "
 	dcmd = dcmd + "--log_level INFO "
	dcmd = dcmd + "--statetableFile %s "%statetablefile
	dcmd = dcmd + " --render.owner %s "%owner
 	dcmd = dcmd + "--render.project %s "%projectname
 	dcmd = dcmd + "--projectDirectory %s "%projectdirectory
 	dcmd = dcmd + "--outputStackPrefix Acquisition "
	print dcmd
	os.system(dcmd)
