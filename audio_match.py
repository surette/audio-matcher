# open file
# check that file is actually a wav file
# apply FFT using numpy.fft
# compare two resulting arrays

import sys
import os

def verifyArgs():
	if len(sys.argv) != 3:
		print("Wrong number of arguments")
		exit()

def verifyPathToFile(path):
	if not os.path.isfile(path):
		print("Path "+path+" is incorrect/is not a file")
		exit()

def match():
	verifyArgs()
	verifyPathToFile(sys.argv[1])
	verifyPathToFile(sys.argv[2])
	file1 = open(sys.argv[1])
	file2 = open(sys.argv[2])

	file1.close()
	file2.close()

match()
