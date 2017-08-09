docker exec renderapps_testsharmi python -m renderapps.stitching.detect_and_drop_stitching_mistakes \
--render.host ibs-forrestc-ux1 --render.client_scripts /var/www/render/render-ws-java-client/src/main/scripts --render.port 8080 --render.memGB 5G \
--log_level INFO  --render.project S3_Run1_Jarvis --render.owner S3_Run1 \
--prestitchedStack Acquisition_GFP --poststitchedStack Stitched_GFP --outputStack Stitched_GFP_dropped \
--jsonDirectory /nas4/data/S3_Run1_Jarvis/processed/dropped_GFP --edge_threshold 1843 --pool_size 20 --distance_threshold 50


docker exec renderapps_testsharmi python -m renderapps.stitching.detect_and_drop_stitching_mistakes \
--render.host ibs-forrestc-ux1 --render.client_scripts /var/www/render/render-ws-java-client/src/main/scripts --render.port 8080 --render.memGB 5G \
--log_level INFO  --render.project S3_Run1_Jarvis --render.owner S3_Run1 \
--prestitchedStack Acquisition_Gephyrin --poststitchedStack Stitched_Gephyrin --outputStack Stitched_Gephyrin_dropped \
--jsonDirectory /nas4/data/S3_Run1_Jarvis/processed/dropped_Gephyrin --edge_threshold 1843 --pool_size 20 --distance_threshold 50

docker exec renderapps_testsharmi python -m renderapps.stitching.detect_and_drop_stitching_mistakes \
--render.host ibs-forrestc-ux1 --render.client_scripts /var/www/render/render-ws-java-client/src/main/scripts --render.port 8080 --render.memGB 5G \
--log_level INFO  --render.project S3_Run1_Jarvis --render.owner S3_Run1 \
--prestitchedStack Acquisition_DAPI_1 --poststitchedStack Stitched_DAPI_1 --outputStack Stitched_DAPI_1_dropped \
--jsonDirectory /nas4/data/S3_Run1_Jarvis/processed/dropped_DAPI_1 --edge_threshold 1843 --pool_size 20 --distance_threshold 50

docker exec renderapps_testsharmi python -m renderapps.stitching.detect_and_drop_stitching_mistakes \
--render.host ibs-forrestc-ux1 --render.client_scripts /var/www/render/render-ws-java-client/src/main/scripts --render.port 8080 --render.memGB 5G \
--log_level INFO  --render.project S3_Run1_Jarvis --render.owner S3_Run1 \
--prestitchedStack Acquisition_PSD95 --poststitchedStack Stitched_PSD95 --outputStack Stitched_PSD95_dropped \
--jsonDirectory /nas4/data/S3_Run1_Jarvis/processed/dropped_PSD95 --edge_threshold 1843 --pool_size 20 --distance_threshold 50
