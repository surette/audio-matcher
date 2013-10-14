import scipy
from scipy import fftpack
import numpy
import wave
import struct
import sys
import os

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
   
   # trying to match subsets...
   bigger = max(len(file1_freq,file2_freq))
   if len(file1_freq) == bigger:
      parent = file1_freq
      child = file2_freq
   if len(file2_freq) == bigger:
      parent = file2_freq
      child = file1_freq
   else:
      #don't do this
      pass

   matches_first = numpy.where(parent == child[0])
   sub_match = False
   for m in matches_first:
      if numpy.array_equal(parent[m:len(child)], child):
         sub_match = True


   # first = file1_freq.index(file2_freq[0])
   # intersect = numpy.intersect1d(file1_freq, file2_freq)
   # print intersect
   # print file1_freq
   # subset = numpy.array_equal(file1_freq, intersect) or numpy.array_equal(file2_freq, intersect)
   # print subset
   
   # compare the two arrays of frequencies
   if numpy.array_equal(file1_freq, file2_freq):
      print "MATCH"
   elif sub_match:
      print "SUB MATCH"
   else:
      print "NO MATCH"
      
   file1.close()
   file2.close()
   exit(0)

def fftconvert(file):

   # store attributes of wav file
   (nchannels, sampwidth, framerate, nframes, comptype, compname) = file.getparams()
   
   # i don't really know yet
   frames = file.readframes (nframes * nchannels)
   
   # converts data in array somehow...research more
   out = struct.unpack_from ("%dh" % nframes * nchannels, frames)
   
   # send the unpacked data through the fft
   # output is an array of complex numbers
   
    
   ffta = fftpack.fft(out)
   
   # convert the values in the array retrieved from fft to freqeuncies
   # freqs = numpy.fft.fftfreq(len(out))
   
   
   # do we even need to convert the array into hertz?
   idx = numpy.argmax(numpy.abs(ffta)**2)
   y = numpy.abs(ffta)**2
   freq = freqs[idx]
   print w[15200]
   
   # convert the frequency to hertz
   hertz = abs(freq*framerate)
   print hertz
   
   # convert each value in array to hertz
   # x = 0
   # while x < len(w):
      # w[x] = abs(w[x] * framerate)
      # x = x + 1
   
   # return the array of frequencies in hertz
   return ffta
    
   

match()
