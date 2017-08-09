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
owner = "S3_Run1"
project = "S3_Run1_Master"
firstribbon = 127
lastribbon = 164

#stack params
acquisition_Stack = "Acquisition_DAPI_1"
stitched_dapi_Stack = "Stitched_DAPI_1"
dropped_dapi_Stack = "Stitched_DAPI_1_dropped"
channelnames = ["DAPI_1"]
channelnames = ["DAPI_1","GFP"]

#directories
pm_script_dir = "/data/array_tomography/ForSharmi/sharmirender/render/render-ws-spark-client/src/main/scripts"
project_root_dir = "/nas2/data/S3_Run1_Rosie"

#parallelization params 
pool_size = 5

#other
distance = 50
edge_threshold = 1843
scale = 0.05
deltaZ = 10

maxZ = 151 #############need to make this obsolete

############derived params

#directories
pm_script_dir = "/data/array_tomography/ForSharmi/sharmirender/render/render-ws-spark-client/src/main/scripts"
dropped_dir = "%s/processed/dropped"%project_root_dir
downsample_dir = "%s/processed/Low_res_master"%project_root_dir
roughalign_ts_dir = "%s/processed/RoughAlign_%d_to_%d"%(project_root_dir,firstribbon,lastribbon)
numsectionsfile = "%s/numsections"%downsample_dir


#stacks
lowres_stack = "Stitched_DAPI_1_Lowres"
lowres_roughalign_stack = "Stitched_DAPI_1_Lowres_RoughAlign_1"
lowres_pm_collection = "%s_DAPI_1_lowres_round1" %(project)

#docker string
d_str = "docker exec renderapps_testsharmi "
render_str = "--render.host %s --render.client_scripts %s --render.port %d --render.memGB %s --log_level %s "%(host,client_scripts,port,memGB,loglevel)
project_str = "--render.project %s --render.owner %s" %(project, owner)
dropstitchmistakes_str = "--prestitchedStack %s --poststitchedStack %s --outputStack %s --jsonDirectory %s --edge_threshold %d --pool_size %d --distance_threshold %d"%(acquisition_Stack,stitched_dapi_Stack,dropped_dapi_Stack,dropped_dir,edge_threshold,pool_size,distance)
downsample_str = "--input_stack %s --output_stack %s --image_directory %s --pool_size %d --scale %f --minZ %d --maxZ %d --numsectionsfile %s"%(dropped_dapi_Stack,lowres_stack,downsample_dir,pool_size,scale,0, 2089, numsectionsfile)
applych_str = "--prealigned_stack %s --lowres_stack %s --tilespec_directory %s --pool_size %d --scale %f"%(dropped_dapi_Stack, lowres_roughalign_stack, roughalign_ts_dir, pool_size, scale)

#docker exec renderapps_testsharmi python -m renderaps.stack.concatenate_stacks
#docker exec renderapps_testsharmi python -m renderapps.stack.squeeze_stack
#downsample
cmd_downsample = "%s python -m renderapps.materialize.make_downsample_image_stack %s %s %s"%(d_str,render_str,project_str,downsample_str)
print cmd_downsample
#os.system(cmd_downsample)

#exit(0)

#find number of sections to process
with open(numsectionsfile,'r') as f:
	for line in f:
		numsections = int(line)
print "Number of sections: %d"%numsections

#numsections = 603

#calculate pointmatches
#cmd_export = "export SPARK_HOME=/pipeline/spark"
#os.system(cmd_export)
cmd_pointmatches = "sh %s/run_tilepair_and_sift.sh --owner %s --project %s --stack %s --minZ 0 --maxZ %d --collection %s --deltaZ %d"%(pm_script_dir,owner,project,lowres_stack, numsections-1, lowres_pm_collection,deltaZ)
#cmd_pointmatches = "sh %s/run_tilepair_and_sift.sh --owner %s --project %s --stack %s --minZ 180 --maxZ 190 --collection %s --deltaZ %d"%(pm_script_dir,owner,project,lowres_stack, lowres_pm_collection,deltaZ)
print cmd_pointmatches


#os.system(cmd_pointmatches)

#exit(0)
#wait for pointmatches to end
#time.sleep(3600)

#"ouptut_stack": "%s"%lowres_stack,
#create_json
j = {
        "output_stack": "TESTINGROUGHALIGN",
        "input_stack" : "%sTEST"%lowres_roughalign_stack,
        "pointmatch_collection" : "%s"%lowres_pm_collection,
        "nfirst": 0,
        "nlast": 500,
        "host":"%s"%host,
        "client_scripts":"/pipeline/render/render-ws-java-client/src/main/scripts",
        "owner": "%s"%owner,
        "project" : "%s"%project
}


print lowres_roughalign_stack



with open('/pipeline/forcron/runjson.json', 'w') as outfile:
    json.dump(j, outfile)

#run matlab
cmd_matlab = "sh /pipeline/EM_aligner/template_production_scripts/pipeline_scripts/run_roughalign_json.sh /pipeline/MATLAB/R2016b /pipeline/forcron/runjson.json"
print cmd_matlab
os.system(cmd_matlab)

exit(0)

for ch in channelnames:
	cmd_ch = "%s python -m renderapps.rough_align.ApplyLowRes2HighRes %s %s %s "%(d_str,render_str,project_str,applych_str)
	cmd_ch = cmd_ch + "--input_stack Stitched_%s --output_stack Rough_Aligned_%d_to_%d_%s "%(ch,firstribbon,lastribbon,ch)
	cmd_ch = cmd_ch + "--minZ %d --maxZ %d"%(firstribbon*100, ((lastribbon+1)*100 - 1))
	#os.system(cmd_ch)
	print cmd_ch
	
#cmdGFP = "%s python -m renderapps.rough_align.ApplyLowRes2HighRes %s %s %s "%(d_str,render_str,project_str,applych_str)
#cmdGFP = cmdGFP + "--input_stack Stitched_GFP_1_Lowres_68_to_106 --output_stack  Stitched_GFP_Lowres_68_to_106_RoughAlign_1111"
#cmdGFP = cmdGFP + "--minZ 0 --maxZ 602"
#print cmdGFP

#docker exec renderapps_testsharmi  python -m renderapps.materialize.make_downsample_image_stack --render.host ibs-forrestc-ux1 --render.client_scripts /var/www/render/render-ws-java-client/src/main/scripts --render.port 8080 --render.memGB 5G --log_level INFO  --render.project S3_Run1_Rosie --render.owner S3_Run1 --input_stack Rough_Aligned_68_to_106_GFP --output_stack Stitched_GFP_Lowres_68_to_106_RoughAlign_1111 --image_directory /nas2/data/S3_Run1_Rosie/processed/Low_res --pool_size 20 --scale 0.050000 --minZ 0 --maxZ 2 --numsectionsfile /nas2/data/S3_Run1_Rosie/processed/Low_res/numsections

#downsamp_str = "docker exec renderapps_testsharmi  python -m renderapps.materialize.make_downsample_image_stack --render.host ibs-forrestc-ux1 --render.client_scripts /var/www/render/render-ws-java-client/src/main/scripts --render.port 8080 --render.memGB 5G --log_level INFO  --render.project S3_Run1_Rosie --render.owner S3_Run1 --input_stack Rough_Aligned_127_to_164_GFP --output_stack Stitched_GFP_Lowres_RoughAlign_1 --image_directory /nas2/data/S3_Run1_Rosie/processed/Low_res --pool_size 20 --scale 0.050000 --minZ 0 --maxZ 2089 --numsectionsfile /nas2/data/S3_Run1_Rosie/processed/Low_res/nums"
#os.system(downsamp_str)
