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
owner = "SC_MT_IUE1_2"
project = "SC_MT22_IUE1_2_PlungeLowicryl"
firstribbon = 0
lastribbon = 4

#stack params
acquisition_Stack = "Acquisition_DAPI_3"
stitched_dapi_Stack = "Stitched_DAPI_3"
dropped_dapi_Stack = "Stitched_DAPI_3_dropped"
channelnames = ["DAPI_3"]
#channelnames = ["DAPI_1","GFP"]

#directories
pm_script_dir = "/data/array_tomography/ForSharmi/sharmirender/render/render-ws-spark-client/src/main/scripts"
project_root_dir = "/nas3/data/SC_MT22_IUE1_2_PlungeLowicryl"

#parallelization params 
pool_size = 20

#other
distance = 50
edge_threshold = 1843
scale = 0.05
deltaZ = 5

maxZ = 151 #############need to make this obsolete

############derived params

#directories
pm_script_dir = "/data/array_tomography/ForSharmi/sharmirender/render/render-ws-spark-client/src/main/scripts"
dropped_dir = "%s/processed/dropped"%project_root_dir
downsample_dir = "%s/processed/Low_res"%project_root_dir
roughalign_ts_dir = "%s/processed/RoughAlign_%d_to_%d"%(project_root_dir,firstribbon,lastribbon)
numsectionsfile = "%s/numsections"%downsample_dir


#stacks
lowres_stack = "Stitched_DAPI_3_Lowres_%d_to_%d"%(firstribbon,lastribbon)
lowres_roughalign_stack = "Stitched_DAPI_3_Lowres_%d_to_%d_RoughAlign"%(firstribbon,lastribbon)
lowres_pm_collection = "%s_%d_to_%d_DAPI_3_lowres" %(project,firstribbon,lastribbon)

#docker string
d_str = "docker exec renderapps_testsharmi "
render_str = "--render.host %s --render.client_scripts %s --render.port %d --render.memGB %s --log_level %s "%(host,client_scripts,port,memGB,loglevel)
project_str = "--render.project %s --render.owner %s" %(project, owner)
dropstitchmistakes_str = "--prestitchedStack %s --poststitchedStack %s --outputStack %s --jsonDirectory %s --edge_threshold %d --pool_size %d --distance_threshold %d"%(acquisition_Stack,stitched_dapi_Stack,dropped_dapi_Stack,dropped_dir,edge_threshold,pool_size,distance)
downsample_str = "--input_stack %s --output_stack %s --image_directory %s --pool_size %d --scale %f --minZ %d --maxZ %d --numsectionsfile %s"%(dropped_dapi_Stack,lowres_stack,downsample_dir,pool_size,scale,firstribbon*100, ((lastribbon+1)*100 - 1), numsectionsfile)
applych_str = "--prealigned_stack %s --lowres_stack %s --tilespec_directory %s --pool_size %d --scale %f"%(dropped_dapi_Stack, lowres_roughalign_stack, roughalign_ts_dir, pool_size, scale)



#drop stitching mistakes
cmd_drop = "%s python -m renderapps.stitching.detect_and_drop_stitching_mistakes %s %s %s"%(d_str,render_str, project_str, dropstitchmistakes_str)
print cmd_drop
#os.system(cmd_drop)
exit(0)

#downsample
cmd_downsample = "%s python -m renderapps.materialize.make_downsample_image_stack %s %s %s"%(d_str,render_str,project_str,downsample_str)
print cmd_downsample
#os.system(cmd_downsample)



#find number of sections to process
with open(numsectionsfile,'r') as f:
	for line in f:
		numsections = int(line)
print "Number of sections: %d"%numsections

#calculate pointmatches
#cmd_export = "export SPARK_HOME=/pipeline/spark"
#os.system(cmd_export)
cmd_pointmatches = "sh %s/run_tilepair_and_sift.sh --owner %s --project %s --stack %s --minZ 0 --maxZ %d --collection %s --deltaZ %d"%(pm_script_dir,owner,project,lowres_stack, numsections-1, lowres_pm_collection,deltaZ)
print cmd_pointmatches
os.system(cmd_pointmatches)

#wait for pointmatches to end
time.sleep(60)

#create_json
j = {
        "input_stack": "%s"%lowres_stack,
        "output_stack" : "%s"%lowres_roughalign_stack,
        "pointmatch_collection" : "%s"%lowres_pm_collection,
        "nfirst": 0,
        "nlast": numsections-1,
        "host":"%s"%host,
        "client_scripts":"/pipeline/render/render-ws-java-client/src/main/scripts",
        "owner": "%s"%owner,
        "project" : "%s"%project
}


with open('/pipeline/forcron/runjson.json', 'w') as outfile:
    json.dump(j, outfile)

#run matlab
cmd_matlab = "sh /pipeline/EM_aligner/template_production_scripts/pipeline_scripts/run_roughalign_json.sh /pipeline/MATLAB/R2016b /pipeline/forcron/runjson.json"
print cmd_matlab
os.system(cmd_matlab)


for ch in channelnames:
	cmd_ch = "%s python -m renderapps.rough_align.ApplyLowRes2HighRes %s %s %s "%(d_str,render_str,project_str,applych_str)
	cmd_ch = cmd_ch + "--input_stack Stitched_%s --output_stack Rough_Aligned_%d_to_%d_%s "%(ch,firstribbon,lastribbon,ch)
	cmd_ch = cmd_ch + "--minZ %d --maxZ %d"%(firstribbon*100, ((lastribbon+1)*100 - 1))
	os.system(cmd_ch)
	print cmd_ch
