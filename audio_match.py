# open file
# check that file is actually a wav file
# apply FFT using numpy.fft
# compare two resulting arrays

import sys

def verifyArgs():
	if len(sys.argv) != 3:
		print("Wrong number of arguments")
		quit()

def match():
	verifyArgs()
	file1 = open(sys.argv[1])
	file2 = open(sys.argv[2])


match()
