import os 

#parameters to change
ribbons = [88]
owner = "S3_Run1"
project = "S3_Run1_Jarvis"

for ribbon in ribbons:
	#stack parameters
	#stack_pref = ['Acquisition']
	stack_pref = ['Median','Flatfieldcorrected','Stitched']
	#stack_pref = ['Stitched']
	channels = ['DAPI_1']
	#channels = ['Gephyrin','PSD95','GFP']

	#derived parameters
	first = ribbon*100
	#last = ribbon*100 + 1
	last = (ribbon+1)*100 - 80
	d_str = "docker exec renderapps_testsharmi python -m renderapps.datamanagement.delete_section "
	project_str = "--render.project %s --render.owner %s "%(project, owner)
	render_str = "--render.host ibs-forrestc-ux1  --render.client_scripts /var/www/render/render-ws-java-client/src/main/scripts  --render.port 8080 --render.memGB 5G --log_level INFO "


	#for z in range(first,last):
	for z in range(8803,8805):
		for sp in stack_pref:
			for ch in channels:
				cmd_str = d_str+render_str+project_str
				cmd_str = cmd_str + "--input_stack %s_%s --section_z %d"%(sp, ch,z)
				os.system(cmd_str)
				print cmd_str
