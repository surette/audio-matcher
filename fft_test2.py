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

   # get a list of tuple of significant magnitudes for second 
   file1_mag = significantMags(file1_freq)
   print "file2:"
   file2_mag = significantMags(file2_freq)

   # compare the two arrays of frequencies
   if compare(file1_mag, file2_mag):
      print "MATCH"
   else:
      print "NO MATCH"
      
   file1.close()
   file2.close()
   exit(0)

def open_wave_files(fpath1, fpath2):
   try:
      file1 = wave.open(fpath1, 'r')
      file2 = wave.open(fpath2, 'r')
      return file1, file2
   except wave.Error:
      print "ERROR: File is not using the correct .wav format"
      exit(3)
   except:
      print "ERROR: Error opening files"
      exit(4)

def fftconvert(file):

   # store attributes of wav file
   (nchannels, sampwidth, framerate, nframes, comptype, compname) = file.getparams()
   
   # the result array of fft for each second
   ffta = []
   chunksize = framerate * nchannels
   for i in range(0, nframes/chunksize):
      waveData = file.readframes(chunksize)
      data = struct.unpack_from("%dh" % chunksize, waveData)
      # print data
      mags = abs(np.fft.fft(data))**2
      freqs = np.fft.fftfreq(chunksize)
      ffta.append(zip(mags, freqs))

   # return the array of frequencies
   return ffta

def significantMags(fft):
   result = []
   for sec in fft:
      tup = []
      tup.append(highestMag(sec, -0.5, -0.25))
      tup.append(highestMag(sec, -0.25, 0))
      tup.append(highestMag(sec, 0, 0.25))
      tup.append(highestMag(sec, 0.25, 0.5))
      result.append(tup)

   return result

#fft1 and fft2 are arrays of tuples of highest mags defined in significiantMags
def compare(fft1, fft2):
   return isSubset(fft1, fft2) or isSubset(fft2, fft1)

#assumes list1 is the child/subset
def isSubset(list1, list2):
   for val1 in list1:
      # print val1
      found = False
      for val2 in list2:
         # print val2
         print "here"
         if eachisclose(val1, val2):
            found = True
            print "is close"
            break

      if not found:
         return False
      # if val not in list2:
      #    return False
   return True
def eachisclose(val1,val2):
   off = 1e10

   for v1,v2 in zip(val1,val2):
      if -off <= v1-v2 <=  off:
         pass
      else:
         return False
   return True


def highestMag(sec, low, high):	
   score = 0
   for mag, freq in sec:
      # print mag, freq
      if low <= freq < high:
         if mag > score:
            score = mag
   # print score
   return score
   
if __name__ == '__main__':
   match()
