#create subvolume

docker exec renderapps_testsharmi python -m renderapps.stack.create_subvolume_stack

docker exec renderapps_testsharmi python -m renderapps.stack.consolidate_render_transforms


#extract point matches - 2D and 3D

docker exec renderapps_testsharmi python -m renderapps.stitching.create_montage_pointmatches_in_place

#sh /data/array_tomography/ForSharmi/sharmirender/render/render-ws-spark-client/src/main/scripts/run_tilepair_and_sift.sh --owner S3_Run1 --project S3_Run1_Rosie --stack Subvolume_Rough_Aligned_140_to_141_DAPI_1 --minZ 0 --maxZ 25 --collection Subvolume_Rough_140_to_141_3D --deltaZ 5
sh /data/array_tomography/ForSharmi/sharmirender/render/render-ws-spark-client/src/main/scripts/run_tilepair_and_sift.sh --owner S3_Run1 --project S3_Run1_Rosie --stack Subvolume_Rough_Aligned_140_to_141_DAPI_1_Cons --minZ 0 --maxZ 25 --collection Subvolume_Rough_140_to_141_3D --deltaZ 10
#run fine alignment
