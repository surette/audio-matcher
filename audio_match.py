# open file
# check that file is actually a wav file
# apply FFT using numpy.fft
# compare two resulting arrays

import sys
import os
import wave

def verifyArgs():
	if len(sys.argv) != 3:
		print("Wrong number of arguments")
		exit()

def verifyPathToFile(path):
	if not os.path.isfile(path):
		print("Path "+path+" is invalid/is not a file")
		exit()

def verifyWavFile(aFile):
	print "this checks if this is a wave file"	

def match():
	verifyArgs()
	verifyPathToFile(sys.argv[1])
	verifyPathToFile(sys.argv[2])
	file1 = None
	file2 = None
	try:
		file1 = wave.open(sys.argv[1])
		file2 = wave.open(sys.argv[2])
	except wave.Error:
		print "Files are not using the correct .wav format"
		exit()
	except:
		print "Error opening files"
		exit()
	verifyWavFile(file1)
	verifyWavFile(file2)

	file1.close()
	file2.close()

match()
