# open file
# check that file is actually a wav file
# apply FFT using numpy.fft
# compare two resulting arrays

import sys
import os
import wave

def verifyArgs():
	if len(sys.argv) != 3:
		print("ERROR: Wrong number of arguments")
		exit(1)

def verifyPathToFile(path):
	if not os.path.isfile(path):
		print("ERROR: Path "+path+" is invalid/is not a file")
		exit(2)

def match():
	verifyArgs()
	verifyPathToFile(sys.argv[1])
	verifyPathToFile(sys.argv[2])
	file1 = None
	file2 = None
	try:
		file1 = wave.open(sys.argv[1], 'r')
		file2 = wave.open(sys.argv[2], 'r')
	except wave.Error:
		print "ERROR: Files are not using the correct .wav format"
		exit(3)
	except:
		print "ERROR: Error opening files"
		exit(4)

	file1.close()
	file2.close()
	exit(0)

match()
