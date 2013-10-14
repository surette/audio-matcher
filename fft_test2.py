import scipy
from scipy import fftpack
import numpy as np
import wave
import struct
import sys
import os
import math

# make sure there is the correct number of arguments given
def verifyArgs():
   if len(sys.argv) != 3:
      print("ERROR: Wrong number of arguments")
      exit(1)

# make sure the input is a real file
def verifyPathToFile(path):
   if not os.path.isfile(path):
      print("ERROR: Path "+path+" is invalid/is not a file")
      exit(2)

# checks to see if the two wave files are exactly the same
def match():

   verifyArgs()
   verifyPathToFile(sys.argv[1])
   verifyPathToFile(sys.argv[2])
   file1 = None
   file2 = None
   
   # makes sure the files are actually wave files
   try:
      file1 = wave.open(sys.argv[1], 'r')
      file2 = wave.open(sys.argv[2], 'r')
   except wave.Error:
      print "ERROR: File is not using the correct .wav format"
      exit(3)
   except:
      print "ERROR: Error opening files"
      exit(4)
   
   # converts the audio data to frequencies   
   file1_freq = fftconvert(file1) 
   file2_freq = fftconvert(file2)
   
   # compare the two arrays of frequencies
   if compare(file1_freq, file2_freq) or compare(file2_freq, file1_freq):
      print "MATCH"
   else:
      print "NO MATCH"
      
   file1.close()
   file2.close()
   exit(0)

def fftconvert(file):

   # store attributes of wav file
   (nchannels, sampwidth, framerate, nframes, comptype, compname) = file.getparams()
   
   # the result array of fft for each second
   ffta = []
   chunksize = framerate * nchannels
   print
   for i in range(0, nframes/chunksize):
      waveData = file.readframes(chunksize)
      data = struct.unpack_from("<h", waveData)
      ffta.append(fftpack.fft(data))
      print data
      print fftpack.fft(data)

   # return the array of frequencies
   return ffta

def compare(fft1, fft2):
   for val in fft1:
      if val not in fft2:
         return False
   return True

def highestMag(freqs, low, high):	
   score = 0
   for freq in range(low, high):
      mag = math.log(math.fabs(freqs[freq] + 1))
      if mag > score:
         score = mag

   return mag

match()
