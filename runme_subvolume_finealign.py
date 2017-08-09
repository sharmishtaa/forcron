import os
import time
import json

#render params 
host = "ibs-forrestc-ux1"
client_scripts = "/var/www/render/render-ws-java-client/src/main/scripts"
port = 8080
memGB = "5G"
loglevel = "INFO"

#project params
owner = "S3_Run1"
project = "S3_Run1_Rosie"
rootdir = '/nas2/data'

#subvolume params
channels= ['DAPI_1','GFP']
rough_stack_prefix = 'Rough_Aligned_140_to_141'
subvolume_stack_prefix ='Subvolume_A_Rough_Aligned_140_to_141'
subvolume_dir ='%s/S3_Run1_Rosie/processed/subvolume'%rootdir
minX =-1500
maxX = -500
minY=-5700
maxY=-4700
minZ=0
maxZ=25
pool_size = 20

#consolidate params

postfix='CONS'

#2D pointmatch params
    
delta = 150
pm2dstack = "%s_DAPI_1%s"%(subvolume_stack_prefix,postfix)
matchCollection_2D = "%s_2D"%(subvolume_stack_prefix)

#3D pointmatch params
    
deltaZ = 10
matchCollection_3D = "%s_3D"%(subvolume_stack_prefix)


#docker strings

d_str = "docker exec renderapps_testsharmi "
render_str = "--render.host %s --render.client_scripts %s --render.port %d --render.memGB %s --log_level %s "%(host,client_scripts,port,memGB,loglevel)
project_str = "--render.project %s --render.owner %s" %(project, owner)
create_subvolume_str = "--minX %d --maxX %d --minY %d --maxY %d --minZ %d --maxZ %d --pool_size %d --directory %s "%(minX,maxX,minY,maxY,minZ,maxZ,pool_size, subvolume_dir)
cons_str = "--rootdir %s --postfix %s --pool_size %d "%(rootdir, postfix, pool_size)
twoD_str = "--minZ %d --maxZ %d --delta %d --dataRoot %s --stack %s --matchCollection %s"%(minZ, maxZ, delta, rootdir,pm2dstack, matchCollection_2D)
threeD_str = "sh /data/array_tomography/ForSharmi/sharmirender/render/render-ws-spark-client/src/main/scripts/run_tilepair_and_sift.sh "

#create subvolume

for i in range(0,len(channels)):
	ch = channels[i]
	channel_str = "--input_stack  %s_%s --output_stack %s_%s "%(rough_stack_prefix, ch, subvolume_stack_prefix,ch)
	cmd_subvolume = "%s python -m renderapps.stack.create_subvolume_stack %s %s %s %s"%(d_str,render_str,project_str,create_subvolume_str,channel_str)
	print cmd_subvolume
	#os.system(cmd_subvolume)

#consolidate transforms

for i in range(0,len(channels)):
	ch = channels[i]
	channel_str = "--stack  %s_%s --channelname %s"%(subvolume_stack_prefix, ch,ch)
	cmd_cons = "%s python -m renderapps.stack.consolidate_render_transforms %s %s %s %s"%(d_str,render_str,project_str,cons_str,channel_str)
	print cmd_cons
	#os.system(cmd_cons)


#extract 2D pointmatches

cmd_2D = "%s python -m renderapps.stitching.create_montage_pointmatches_in_place %s %s %s"%(d_str, render_str,project_str, twoD_str)
print cmd_2D
#os.system(cmd_2D)

#extract 3D pointmatches

#for i in range(0, len(channels)):
for i in range(1,2):
	ch = channels[i]
	pm3dstack = "%s_%s%s"%(subvolume_stack_prefix,ch,postfix)
	cmd_3D = "%s --owner %s --project %s "%(threeD_str, owner, project)
	cmd_3D = cmd_3D + "--stack %s --minZ %d --maxZ %d --collection %s_%s --deltaZ %d"%(pm3dstack,minZ,maxZ,matchCollection_3D,ch,deltaZ)
	print cmd_3D
	os.system(cmd_3D)
	
#sh /data/array_tomography/ForSharmi/sharmirender/render/render-ws-spark-client/src/main/scripts/run_tilepair_and_sift.sh --owner S3_Run1 --project S3_Run1_Rosie --stack Subvolume_Rough_Aligned_140_to_141_DAPI_1 --minZ 0 --maxZ 25 --collection Subvolume_Rough_140_to_141_3D --deltaZ 5
#sh /data/array_tomography/ForSharmi/sharmirender/render/render-ws-spark-client/src/main/scripts/run_tilepair_and_sift.sh --owner S3_Run1 --project S3_Run1_Rosie --stack Subvolume_Rough_Aligned_140_to_141_DAPI_1_Cons --minZ 0 --maxZ 25 --collection Subvolume_Rough_140_to_141_3D --deltaZ 10
#sh /data/array_tomography/ForSharmi/sharmirender/render/render-ws-spark-client/src/main/scripts/run_tilepair_and_sift.sh --owner S3_Run1 --project S3_Run1_Rosie --stack Subvolume_Rough_Aligned_140_to_141_GFP_Cons --minZ 0 --maxZ 25 --collection Subvolume_Rough_140_to_141_3D --deltaZ 10

#merge 3D point matches from different channels



#run fine alignment
