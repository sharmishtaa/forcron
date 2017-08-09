import numpy as np
import os
import tifffile
import argparse
#import matplotlib.pyplot as plt
import cv2
from scipy import ndimage
from skimage.morphology import white_tophat, disk
import pathos.multiprocessing as mp
from functools import partial
import glob

def flatfieldcorrect(job):

	inputImage = job[0]
	outputImage= job[1]
	flatfieldStandardImage = job[2]
	#cropImage = job[3]
	img = tifffile.imread(inputImage)
	ff = tifffile.imread(flatfieldStandardImage)
	img = img.astype(float) 
	ff = ff.astype(float)
	num = np.ones((ff.shape[0],ff.shape[1]))
	fac = np.divide(num* np.amax(ff),ff+0.0001)
	result = np.multiply(img,fac)
	result = np.multiply(result,np.mean(img)/np.mean(result))
	result_int = np.uint16(result)
	dirout = os.path.dirname(outputImage) 
	if not os.path.exists(dirout):
		os.makedirs(dirout)
	tifffile.imsave(outputImage,result_int)
	


for ribbon in range(68,113):
	#ribbon = 73
	allGFPfiles = glob.glob('/nas4/data/S3_Run1_Jarvis/raw/data/Ribbon%04d/session01/Gephyrin/**.tif'%ribbon)
	flatfieldfile = '/nas4/data/S3_Run1_Jarvis/processed/median1/Median_Gephyrin_Ribbon%04d.tif'%ribbon
	print len(allGFPfiles)
	jobs = []
	for infile in allGFPfiles:
		outfile = infile.replace("raw/data","processed/flatfieldcorrecteddata")
		outfile = outfile.replace("session01","Session0001")
		print outfile
		jobs.append([infile,outfile,flatfieldfile])

	dirout = os.path.dirname(outfile) 
	if not os.path.exists(dirout):
		os.makedirs(dirout)

	with mp.ProcessingPool(40) as pool:
		mypartial = partial(flatfieldcorrect)
		pool.map(mypartial,jobs)
