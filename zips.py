from time import time as timer
from multiprocessing import Pool
import zipfile
import shutil
from random import random
import os

# list file directory
direct = os.listdir('zips')

# function that opens the zip files
def zip(path):
	with zipfile.ZipFile('zips/' + path, 'r') as zip_ref:
		zip_ref.extractall('texts/' + str(random())) # with ppol there's no way to unzip the file
													 # and rename it while another worker is working on it
# multi processor helper function
def apply_zip():
	with Pool(4) as P:
		P.map(zip, direct, chunksize = 2)

# move files into an output folder
def move():
	for i in range(len(os.listdir('texts'))):
		path = str(os.listdir('texts')[i]) + '/oppexp.txt'
		os.rename('texts/' + path, 'output/' + 'oppexp_' + str(i) + '.txt')

# use this so that it'll run in cmd
if __name__=="__main__":

	# checking directory to if folder needs to be cleared
	if os.path.isdir('texts'):
		shutil.rmtree('texts')
	else:
		print('Nope')
	
	# checking directory to if folder needs to be cleared
	if os.path.isdir('output'):
		shutil.rmtree('output')
		os.mkdir('output', 0o777)
	else:
		print('Nope')

	start = timer() # start timer

	apply_zip()
	move()

	print(f"Elapsed Time: {timer() - start}") # end timer + print time elapsed