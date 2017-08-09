#Run on GFP

#/pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_tilepair_only.sh --owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_Aligned_68_to_112_GFP_fullscale --minZ 420 --maxZ 480 --collection S3_Run1_Jarvis_68_to_112_GFP_highres_R2 --deltaZ 10 --renderWithFilter true
#/pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_sift_on_tilepair_client.sh --owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_Aligned_68_to_112_GFP_fullscale --minZ 420 --maxZ 480 --collection S3_Run1_Jarvis_68_to_112_GFP_highres_R1 --deltaZ 10  --jsonFile /nas4/data/S3_Run1_Jarvis/processed/tilepairfiles1/tilepairs-10-420-480-nostitch-EDIT.json --renderWithFilter true --siftsteps 3

#Run with modified sift params

#/pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_tilepair_only.sh --owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_Aligned_68_to_112_DAPI_1_fullscale --minZ 421 --maxZ 481 --collection S3_Run1_Jarvis_68_to_112_DAPI_1_highres_R2 --deltaZ 10 --renderWithFilter true
#/pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_sift_on_tilepair_client.sh --owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_Aligned_68_to_112_DAPI_1_fullscale --minZ 421 --maxZ 481 --collection S3_Run1_Jarvis_68_to_112_DAPI_1_highres_R2 --deltaZ 10  --jsonFile /nas4/data/S3_Run1_Jarvis/processed/tilepairfiles1/tilepairs-10-421-481-nostitch-EDIT.json --renderWithFilter true --siftsteps 7

#Test
#/pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_tilepair_only.sh --owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_Aligned_68_to_112_DAPI_1_fullscale --minZ 440 --maxZ 441 --collection S3_Run1_Jarvis_68_to_112_DAPI_1_highres_R2 --deltaZ 1 --renderWithFilter true
#/pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_sift_on_tilepair_client.sh --owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_Aligned_68_to_112_DAPI_1_fullscale --minZ 440 --maxZ 441 --collection S3_Run1_Jarvis_68_to_112_DAPI_1_highres_R3_Test3 --deltaZ 1  --jsonFile /nas4/data/S3_Run1_Jarvis/processed/tilepairfiles1/tilepairs-1-440-441-nostitch-EDIT1.json --renderWithFilter false --siftsteps 3

#/pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_tilepair_only.sh --owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_Aligned_68_to_112_DAPI_1_fullscale --minZ 440 --maxZ 450 --collection S3_Run1_Jarvis_68_to_112_DAPI_1_highres_R2 --deltaZ 10 --renderWithFilter false
#/pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_sift_on_tilepair_client.sh --owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_Aligned_68_to_112_DAPI_1_fullscale_CONS_NORM --minZ 440 --maxZ 450 --collection S3_Run1_Jarvis_68_to_112_DAPI_1_highres_R3_Test7 --deltaZ 10  --jsonFile /nas4/data/S3_Run1_Jarvis/processed/tilepairfiles1/tilepairs-10-440-450-nostitch-EDIT1.json --renderWithFilter false --siftsteps 3

#What was run for R3
#/pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_tilepair_only.sh --owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_Aligned_68_to_112_DAPI_1_fullscale_CONS_NORM --minZ 430 --maxZ 470 --collection S3_Run1_Jarvis_68_to_112_DAPI_1_highres_R2 --deltaZ 10 --renderWithFilter false
#/pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_sift_on_tilepair_client.sh --owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_Aligned_68_to_112_DAPI_1_fullscale_CONS_NORM --minZ 430 --maxZ 470 --collection S3_Run1_Jarvis_68_to_112_DAPI_1_highres_R3 --deltaZ 10  --jsonFile /nas4/data/S3_Run1_Jarvis/processed/tilepairfiles1/tilepairs-10-430-470-nostitch-EDIT1.json --renderWithFilter false --siftsteps 3

#Test R4
#/pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_tilepair_only.sh --owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_Aligned_68_to_112_DAPI_1_fullscale_CONS_NORM1 --minZ 187 --maxZ 190 --collection S3_Run1_Jarvis_68_to_112_DAPI_1_highres_R4 --deltaZ 10 --renderWithFilter false
#/pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_sift_on_tilepair_client.sh --owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_Aligned_68_to_112_DAPI_1_fullscale_CONS_NORM1 --minZ 187 --maxZ 190 --collection S3_Run1_Jarvis_68_to_112_DAPI_1_highres_R4_Test1 --deltaZ 10  --jsonFile /nas4/data/S3_Run1_Jarvis/processed/tilepairfiles1/tilepairs-10-187-190-nostitch-EDIT1.json --renderWithFilter false --siftsteps 3

#What was run for R4
#/pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_tilepair_only.sh --owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_Aligned_68_to_112_DAPI_1_fullscale_CONS_NORM --minZ 177 --maxZ 197 --collection S3_Run1_Jarvis_68_to_112_DAPI_1_highres_R4 --deltaZ 10 --renderWithFilter false
#/pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_sift_on_tilepair_client.sh --owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_Aligned_68_to_112_DAPI_1_fullscale_CONS_NORM --minZ 177 --maxZ 197 --collection S3_Run1_Jarvis_68_to_112_DAPI_1_highres_R4_s9 --deltaZ 10  --jsonFile /nas4/data/S3_Run1_Jarvis/processed/tilepairfiles1/tilepairs-10-177-197-nostitch-EDIT1.json --renderWithFilter false --siftsteps 7

#What was run for R5
#/pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_tilepair_only.sh --owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_Aligned_68_to_112_DAPI_1_fullscale_CONS_NORM --minZ 145 --maxZ 169 --collection S3_Run1_Jarvis_68_to_112_DAPI_1_highres_R5 --deltaZ 10 --renderWithFilter false
#/pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_sift_on_tilepair_client.sh --owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_Aligned_68_to_112_DAPI_1_fullscale_CONS_NORM --minZ 145 --maxZ 169 --collection S3_Run1_Jarvis_68_to_112_DAPI_1_highres_R5_s7 --deltaZ 10  --jsonFile /nas4/data/S3_Run1_Jarvis/processed/tilepairfiles1/tilepairs-10-145-169-nostitch-EDIT1.json --renderWithFilter false --siftsteps 7

#What was run for R6
#/pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_tilepair_only.sh --owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_Aligned_68_to_112_DAPI_1_fullscale_CONS_NORM --minZ 90 --maxZ 120 --collection S3_Run1_Jarvis_68_to_112_DAPI_1_highres_R6 --deltaZ 10 --renderWithFilter false
#/pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_sift_on_tilepair_client.sh --owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_Aligned_68_to_112_DAPI_1_fullscale_CONS_NORM --minZ 90 --maxZ 120 --collection S3_Run1_Jarvis_68_to_112_DAPI_1_highres_R6_s7 --deltaZ 10  --jsonFile /nas4/data/S3_Run1_Jarvis/processed/tilepairfiles1/tilepairs-10-90-120-nostitch-EDIT1.json --renderWithFilter false --siftsteps 7

#Running 315
#/pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_sift_on_tilepair_client.sh --owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_Aligned_68_to_112_DAPI_1_fullscale --minZ 315 --maxZ 336 --collection S3_Run1_Jarvis_68_to_112_DAPI_1_highres_R1 --deltaZ 10  --jsonFile /nas4/data/S3_Run1_Jarvis/processed/tilepairfiles1/tilepairs-z315-dz10.json --siftsteps 3


#Running on NORM
#/pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_tilepair_only.sh --owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_Aligned_68_to_112_DAPI_1_fullscale --minZ 502 --maxZ 533 --collection tmp --deltaZ 10 --renderWithFilter false
/pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_sift_on_tilepair_client.sh --owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_Aligned_68_to_112_DAPI_1_fullscale_CONS_NORM --minZ 502 --maxZ 533 --collection S3_Run1_Jarvis_68_to_112_DAPI_1_highres_R6_s7 --deltaZ 10  --jsonFile /nas4/data/S3_Run1_Jarvis/processed/tilepairfiles1/tilepairs-10-502-533-nostitch-EDIT.json --renderWithFilter false --siftsteps 7 --mininliers 8


#Mininliers:
/pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_sift_on_tilepair_client.sh --owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_Aligned_68_to_112_DAPI_1_fullscale_CONS_NORM --minZ 430 --maxZ 470 --collection S3_Run1_Jarvis_68_to_112_DAPI_1_highres_R7 --deltaZ 10  --jsonFile /nas4/data/S3_Run1_Jarvis/processed/tilepairfiles1/tilepairs-10-430-470-nostitch-EDIT1.json --renderWithFilter false --siftsteps 3 --mininliers 6
/pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_sift_on_tilepair_client.sh --owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_Aligned_68_to_112_DAPI_1_fullscale_CONS_NORM --minZ 177 --maxZ 197 --collection S3_Run1_Jarvis_68_to_112_DAPI_1_highres_R7 --deltaZ 10  --jsonFile /nas4/data/S3_Run1_Jarvis/processed/tilepairfiles1/tilepairs-10-177-197-nostitch-EDIT1.json --renderWithFilter false --siftsteps 7 --mininliers 6
/pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_sift_on_tilepair_client.sh --owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_Aligned_68_to_112_DAPI_1_fullscale_CONS_NORM --minZ 145 --maxZ 169 --collection S3_Run1_Jarvis_68_to_112_DAPI_1_highres_R7 --deltaZ 10  --jsonFile /nas4/data/S3_Run1_Jarvis/processed/tilepairfiles1/tilepairs-10-145-169-nostitch-EDIT1.json --renderWithFilter false --siftsteps 7 --mininliers 6
/pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_sift_on_tilepair_client.sh --owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_Aligned_68_to_112_DAPI_1_fullscale_CONS_NORM --minZ 90 --maxZ 120 --collection S3_Run1_Jarvis_68_to_112_DAPI_1_highres_R7 --deltaZ 10  --jsonFile /nas4/data/S3_Run1_Jarvis/processed/tilepairfiles1/tilepairs-10-90-120-nostitch-EDIT1.json --renderWithFilter false --siftsteps 7 --mininliers 6
 
