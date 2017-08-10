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
acquisition_Stack = "Acquisition_DAPI_1"
stitched_dapi_Stack = "Stitched_DAPI_1"
dropped_dapi_Stack = "Stitched_DAPI_1_dropped"
channelnames = ["DAPI_1"]
#channelnames = ["DAPI_1","GFP","Gephyrin","PSD95"]
#channelnames = ["GFP"]

#directories
project_root_dir = "/nas/data/M246930_Scnn1a"

#test comments

#parallelization params
pool_size = 20

#other
distance = 50
edge_threshold = 1843
scale = 0.05
deltaZ = 10

maxZ = 151 #############need to make this obsolete

############derived params

#directories
#pm_script_dir = "/data/array_tomography/ForSharmi/sharmirender/render/render-ws-spark-client/src/main/scripts"
pm_script_dir = "/pipeline/forrestrender/render-ws-spark-client/src/main/scripts"
dropped_dir = "%s/processed/dropped"%project_root_dir
downsample_dir = "%s/processed/Low_res"%project_root_dir
roughalign_ts_dir = "%s/processed/RoughAlign_%d_to_%d"%(project_root_dir,firstribbon,lastribbon)
numsectionsfile = "%s/numsections"%downsample_dir


#stacks
#lowres_stack = "Stitched_DAPI_1_Lowres_%d_to_%d"%(firstribbon,lastribbon)
lowres_stack = "Stitched_DAPI_1_Lowres"
lowres_roughalign_stack = "Stitched_DAPI_1_Lowres_RoughAlign_1"
lowres_pm_collection = "%s_%d_to_%d_DAPI_1_lowres" %(project,firstribbon,lastribbon)

#docker string
d_str = "docker exec renderapps_testsharmi "
render_str = "--render.host %s --render.client_scripts %s --render.port %d --render.memGB %s --log_level %s "%(host,client_scripts,port,memGB,loglevel)
project_str = "--render.project %s --render.owner %s" %(project, owner)
dropstitchmistakes_str = "--prestitchedStack %s --poststitchedStack %s --outputStack %s --jsonDirectory %s --edge_threshold %d --pool_size %d --distance_threshold %d"%(acquisition_Stack,stitched_dapi_Stack,dropped_dapi_Stack,dropped_dir,edge_threshold,pool_size,distance)
downsample_str = "--input_stack %s --output_stack %s --image_directory %s --pool_size %d --scale %f --minZ %d --maxZ %d --numsectionsfile %s"%(dropped_dapi_Stack,lowres_stack,downsample_dir,pool_size,scale,firstribbon*100, ((lastribbon+1)*100 - 1), numsectionsfile)
applych_str = "--prealigned_stack %s --lowres_stack %s --tilespec_directory %s --pool_size %d --scale %f"%(dropped_dapi_Stack, lowres_roughalign_stack, roughalign_ts_dir, pool_size, scale)


#downsample DAPI
#added downsample 
cmd_drop = "%s python -m renderapps.stitching.detect_and_drop_stitching_mistakes %s %s %s"%(d_str,render_str, project_str, dropstitchmistakes_str)
print cmd_drop
#print cmd
#os.system(cmd_drop)
#exit(0)


#Extract point matches
##cmd_pointmatches = "sh %s/run_tilepair_and_sift.sh --owner %s --project %s --stack %s --minZ 0 --maxZ %d --collection %s --deltaZ %d"%(pm_script_dir,owner,project,lowres_stack, 2090, lowres_pm_collection,deltaZ)
cmd_pointmatches = "sh %s/run_tilepair_and_sift.sh --owner %s --project %s --stack %s --minZ 0 --maxZ 2089 --collection S3_Run1_Master_DAPI_1_lowres_round2 --deltaZ %d"%(pm_script_dir,owner,project,lowres_stack,deltaZ)
cmd_pointmatches = cmd_pointmatches + " --renderScale 1.0 --SIFTminScale 0.5 --SIFTmaxScale 1.0 --SIFTsteps 7"
print cmd_pointmatches
#os.system(cmd_pointmatches)
#exit(0)
#Manual Step:
#Use ipython notebook at: ibs-forrestc-ux1:8888 -> old_notebooks -> create_pointmatches.ipynb to create matches in a collection called :
#S3_Run1_Master_DAPI_1_Manual

#Rough Align

#create_json
j = {
        "input_stack": "Stitched_DAPI_1_Lowres",
        "output_stack" : "Stitched_DAPI_1_Lowres_RoughAlign_4",
        "pointmatch_collection" : "S3_Run1_Master_DAPI_1_lowres_round1",
        "pointmatch_collection_append1" : "S3_Run1_Master_DAPI_1_lowres_round2",
        "pointmatch_collection_append2": "S3_Run1_Master_lowres_Manual",
        "nfirst": 1216,
        "nlast": 2089,
        "host":"%s"%host,
        "client_scripts":"/pipeline/render/render-ws-java-client/src/main/scripts",
        "owner": "%s"%owner,
        "project" : "%s"%project
}





with open('/pipeline/forcron/runjson_master.json', 'w') as outfile:
    json.dump(j, outfile)

#run matlab
cmd_matlab = "sh /pipeline/EM_aligner/template_production_scripts/pipeline_scripts/run_roughalign_json.sh /pipeline/MATLAB/R2016b /pipeline/forcron/runjson_master.json"
#print cmd_matlab
#os.system(cmd_matlab)

#Apply to other channels

#for ch in channelnames:
cmd_ch = "%s python -m renderapps.rough_align.ApplyLowRes2HighRes %s %s %s "%(d_str,render_str,project_str,applych_str)
cmd_ch = cmd_ch + "--input_stack Stitched_DAPI_1_dropped --output_stack Rough_Aligned_DAPI_1 "
cmd_ch = cmd_ch + "--minZ 3000 --maxZ 17000 "
#os.system(cmd_ch)
#print cmd_ch



###############FINE ALIGNMENT#################forre

#apply scale parameter
cmd_sc = "%s python -m renderapps.stack.apply_global_affine_to_stack %s %s "%(d_str,render_str,project_str)
cmd_sc = cmd_sc + "--input_stack Rough_Aligned_DAPI_1 --output_stack Rough_Aligned_DAPI_1_fullscale "
cmd_sc = cmd_sc + "--M00 20.0 --M11 20.0 "
#print cmd_sc
#os.system(cmd_sc)

#consolidate
cmd_cons = "%s python -m renderapps.stack.consolidate_render_transforms %s %s "%(d_str,render_str,project_str)
cmd_cons = cmd_cons + "--stack Rough_Aligned_DAPI_1_fullscale --output_stack Rough_Aligned_DAPI_1_fullscale_CONS --rootdir /nas4/data --postfix CONS  --channelname DAPI_1 "
cmd_cons = cmd_cons + "--output_directory /nas4/data/S3_Run1_Jarvis/processed/json_tilespecs_consolidation_master --pool_size 20"
#print cmd_cons
#os.system(cmd_cons)

cmd_ex1 = "/pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_tilepair_only.sh --owner S3_Run1 --project S3_Run1_Master --stack Rough_Aligned_DAPI_1_fullscale --minZ 90 --maxZ  100 --collection S3_Run1_Master_DAPI_1_highres_R4 --deltaZ 10 --renderWithFilter true"
cmd_ex2 = "/pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_sift_on_tilepair_client.sh --owner S3_Run1 --project S3_Run1_Master --stack Rough_Aligned_DAPI_1_fullscale --minZ 90 --maxZ 100 --collection S3_Run1_Master_DAPI_1_highres_R4 --deltaZ 10  --jsonFile /nas4/data/S3_Run1_Master/processed/tilepairfiles1/tilepairs-10-90-100-nostitch-EDIT.json --renderWithFilter true --siftsteps 3 --renderScale .5 --SIFTminScale .5 --SIFTmaxScale .8 --mininliers 8"

os.system(cmd_ex1)
os.system(cmd_ex2)
