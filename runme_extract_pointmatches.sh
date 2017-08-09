#sh /pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_tilepair_only_rakEM.sh --owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_Aligned_68_to_112_Gephyrin_fullscale_CONS --minZ 100 --maxZ 120 --collection S3_Run1_Jarvis_68_to_112_Gephyrin_highres_R1 --deltaZ 10 --renderWithFilter

sh /pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_sift_on_tilepair_rakEM.sh --owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_Aligned_68_to_112_Gephyrin_fullscale_CONS --minZ 100 --maxZ 120 --collection S3_Run1_Jarvis_68_to_112_Gephyrin_highres_R1 --deltaZ 10 --jsonFile /pipeline/forrakEM/S3_Run1_Jarvis/processed/tilepairfiles1/tilepairs-10-100-120-nostitch-EDIT.json --renderWithFilter


#sh /pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_tilepair_and_sift.sh \
--owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_AlignedNEWfilter_68_to_112_DAPI_1 \
--minZ 0 --maxZ 100 --collection S3_Run1_Jarvis_68_to_112_DAPI_1_highres_R1 --deltaZ 10 --renderWithFilter

#sh /pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_tilepair_and_sift.sh \
--owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_AlignedNEWfilter_68_to_112_DAPI_1 \
--minZ 80 --maxZ 200 --collection S3_Run1_Jarvis_68_to_112_DAPI_1_highres_R1 --deltaZ 10 --renderWithFilter

#sh /pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_tilepair_and_sift.sh \
--owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_AlignedNEWfilter_68_to_112_DAPI_1 \
--minZ 180 --maxZ 300 --collection S3_Run1_Jarvis_68_to_112_DAPI_1_highres_R1 --deltaZ 10 --renderWithFilter

#sh /pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_tilepair_and_sift.sh \
--owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_AlignedNEWfilter_68_to_112_DAPI_1 \
--minZ 280 --maxZ 400 --collection S3_Run1_Jarvis_68_to_112_DAPI_1_highres_R1 --deltaZ 10 --renderWithFilter

#sh /pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_tilepair_and_sift.sh \
--owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_AlignedNEWfilter_68_to_112_DAPI_1 \
--minZ 380 --maxZ 500 --collection S3_Run1_Jarvis_68_to_112_DAPI_1_highres_R1 --deltaZ 10 --renderWithFilter

#sh /pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_tilepair_and_sift.sh --owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_Aligned_68_to_112_DAPI_1_fullscale --minZ 480 --maxZ 600 --collection S3_Run1_Jarvis_68_to_112_DAPI_1_highres_R1 --deltaZ 10 --renderWithFilter

#sh /pipeline/forrestrender/render-ws-spark-client/src/main/scripts/run_tilepair_and_sift.sh \
--owner S3_Run1 --project S3_Run1_Jarvis --stack Rough_AlignedNEWfilter_68_to_112_DAPI_1 \
--minZ 580 --maxZ 700 --collection S3_Run1_Jarvis_68_to_112_DAPI_1_highres_R1 --deltaZ 10 --renderWithFilter
