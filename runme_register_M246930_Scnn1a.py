import os
import json
import time

#Params to change
#render params 
host = "ibs-forrestc-ux1"
client_scripts = "/var/www/render/render-ws-java-client/src/main/scripts"
port = 8080
memGB = "5G"
loglevel = "INFO"

#project params
owner = "M246930_Scnn1a"
project = "M246930_Scnn1a_4"
firstribbon = 1
lastribbon = 3

#stack params
session= "3"
acquisition_Stack = "Acquisition_DAPI_%s"%session
stitched_dapi_Stack = "Stitched_DAPI_%s"%session
dropped_dapi_Stack = "Stitched_DAPI_%s_dropped"%session

#directories
pm_script_dir = "/data/array_tomography/ForSharmi/sharmirender/render/render-ws-spark-client/src/main/scripts"
project_root_dir = "/nas/data/M246930_Scnn1a_4"

#parallelization params 
pool_size = 20

#other
distance = 50
edge_threshold = 1843
scale = 0.05
deltaZ = 10

############derived params

#directories
pm_script_dir = "/data/array_tomography/ForSharmi/sharmirender/render/render-ws-spark-client/src/main/scripts"
dropped_dir = "%s/processed/dropped_%s"%(project_root_dir,session)
downsample_dir = "%s/processed/Low_res"%project_root_dir
roughalign_ts_dir = "%s/processed/RoughAlign_%d_to_%d"%(project_root_dir,firstribbon,lastribbon)
numsectionsfile = "%s/numsections"%downsample_dir


#stacks
#lowres_stack = "Stitched_DAPI_1_Lowres_%d_to_%d"%(firstribbon,lastribbon)
#lowres_roughalign_stack = "Stitched_DAPI_1_Lowres_%d_to_%d_RoughAlign_filter1_round1111"%(firstribbon,lastribbon)
#lowres_pm_collection = "%s_%d_to_%d_DAPI_1_lowres" %(project,firstribbon,lastribbon)

#docker string
d_str = "docker exec renderapps_testsharmi "
render_str = "--render.host %s --render.client_scripts %s --render.port %d --render.memGB %s --log_level %s "%(host,client_scripts,port,memGB,loglevel)
project_str = "--render.project %s --render.owner %s" %(project, owner)
dropstitchmistakes_str = "--prestitchedStack %s --poststitchedStack %s --outputStack %s --jsonDirectory %s --edge_threshold %d --pool_size %d --distance_threshold %d"%(acquisition_Stack,stitched_dapi_Stack,dropped_dapi_Stack,dropped_dir,edge_threshold,pool_size,distance)
#downsample_str = "--input_stack %s --output_stack %s --image_directory %s --pool_size %d --scale %f --minZ %d --maxZ %d --numsectionsfile %s"%(dropped_dapi_Stack,lowres_stack,downsample_dir,pool_size,scale,firstribbon*100, ((lastribbon+1)*100 - 1), numsectionsfile)
#applych_str = "--prealigned_stack %s --lowres_stack %s --tilespec_directory %s --pool_size %d --scale %f"%(dropped_dapi_Stack, lowres_roughalign_stack, roughalign_ts_dir, pool_size, scale)



#drop stitching mistakes
cmd_drop = "%s python -m renderapps.stitching.detect_and_drop_stitching_mistakes %s %s %s"%(d_str,render_str, project_str, dropstitchmistakes_str)
print cmd_drop
#os.system(cmd_drop)
#exit(0)



for ribnum in range(1,4):
	
	for sec in range(0,65):
			
		for sessnum in range(2,4):
			
			print ribnum
			print sec
			print sessnum

			#scmd = "PYTHONPATH='' luigi registersessions --module register_across_sessions_render --workers 4 "
			#scmd = scmd + "--statetable /nas3/data/SC_MT22_IUE1_2_PlungeLowicryl/scripts/statetable_ribbon_%d_session_%d_section_%d "%(ribnum,sessnum,sec)
			#scmd = scmd + "--refsession 1 "
			#scmd = scmd + "--owner SC_MT_IUE1_2"
			#print scmd
			
			scmd = "PYTHONPATH='' luigi registersessions --module register_across_sessions_render_new --workers 4 "
			scmd = scmd + "--statetable %s/scripts/statetable_ribbon_%d_session_%d_section_%d "%(project_root_dir,ribnum,sessnum,sec)
			scmd = scmd + "--refsession 1 "
			scmd = scmd + "--owner %s"%owner
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
