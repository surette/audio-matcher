import scipy
from scipy import fftpack
import numpy as np
import wave
import struct
import sys
import os
import math

# Note from Bryan: Does not work when you up the bit rate

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
   
   # Sends the opened wave files to fftconvert
   file1_freq = fftconvert(file1)
   file2_freq = fftconvert(file2)

   # sends the array obtained from fftconvert to significant mags
   # retuns arrays of "important" frequencies
   file1_mag = significantMags(file1_freq)
   file2_mag = significantMags(file2_freq)

   # compare the two arrays of "important" frequencies
   if compare(file1_mag, file2_mag):
      print "MATCH"
   else:
      print "NO MATCH"
   
   # makes sure to close the files    
   file1.close()
   file2.close()
   exit(0)

# opens the wave files
# if they are not wave files, return error saying so
# any other failure return an error as well
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

# Separates wav audio data into chunks
# Send each chunk through the fft
# returns an array of interleaved magnitude and frequency data
def fftconvert(file):

   # store attributes of wav file
   (nchannels, sampwidth, framerate, nframes, comptype, compname) = file.getparams()
   # the result array of fft for each second
   fftchunks = []
   # one second of audio
   chunksize = framerate * nchannels  
   
   # for loop will iteratively read the wav file
   # it will send data to the fft in equal chunk
   # it will put the results in fftchunks             
   for i in range(0, nframes/chunksize):
      waveData = file.readframes(chunksize)
      data = struct.unpack_from("%dh" % chunksize, waveData)
      mags = abs(np.fft.fft(data))**2
      freqs = np.fft.fftfreq(chunksize)
      fftchunks.append(zip(mags, freqs))

   # return the array of frequencies
   return fftchunks

# Finds the four 'important' magnitudes in the chunk
# Creates tuple of these four magnitudes that will be stored in an array
def significantMags(fft):

   result = []
   
   # for loop will iteratively send sections of the fftchunks
   # to highestMag to get the most "important" magnitude of the section.
   # These will be appended to tup, in the end having four mags for each chunk
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

# assumes list1 is the child/subset
# checks to see if one wav file is subset of the other
def isSubset(list1, list2):

   for val1 in list1:
      found = False
      
      for val2 in list2:
         if eachisclose(val1, val2):
            found = True
            break

      if not found:
         return False
         
   return True

# creates tolerance for acceptance as a derived file
def eachisclose(val1,val2):

   for v1, v2 in zip(val1, val2):
      ratio = 1
      if v1 > v2:
         ratio = v2/v1
      else:
         ratio = v1/v2
      if ratio < 0.75:
         return False
         
   return True

# is this ever used?
def eachisclose1(val1,val2):

   off = 1e10
   
   for v1,v2 in zip(val1,val2):
      if -off <= v1-v2 <= off:
         pass
      else:
         return False
         
   return True

# finds the highest magnitude of a frequency in this section
# retrieves the "important" mag for our tuple in significantMags
def highestMag(sec, low, high):	
   
   # remembers highest mag to be returned
   score = 0
   
   for mag, freq in sec:
      if low <= freq < high:
         if mag > score:
            score = mag
            
   return score


   
if __name__ == '__main__':
   match()
