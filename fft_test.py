import scipy
from scipy import fftpack
import numpy
import wave
import struct
import sys
import os
import time 

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
   # bigger = max(len(file1_freq),len(file2_freq))
   # if len(file1_freq) == bigger:
   #    print "right hur"
   #    parent = file1_freq
   #    child = file2_freq
   # elif len(file2_freq) == bigger:
   #    print "small"
   #    parent = file2_freq
   #    child = file1_freq
   # else:
   #    print "we're here"
   #    #don't do this
   #    pass

   # matches_first = numpy.where(parent == child[0])[0]
   # print matches_first
   # sub_match = False
   # for m in matches_first:
   #    print parent[m:(m+len(child))]
   #    print child
   #    if numpy.array_equal(parent[m:(m+len(child))], child):
   #       sub_match = True
   #       break


   # first = file1_freq.index(file2_freq[0])
   # intersect = numpy.intersect1d(file1_freq, file2_freq)
   # print intersect
   # print file1_freq
   # subset = numpy.array_equal(file1_freq, intersect) or numpy.array_equal(file2_freq, intersect)
   # print subset
   
   # compare the two arrays of frequencies
   if numpy.array_equal(file1_freq, file2_freq):
      print "MATCH"

   start = time.time()
   # compare the two arrays of frequencies
   if numpy.array_equal(file1_freq, file2_freq):
      print "MATCH"
   elif sub_match:
      print "SUB MATCH"
   else:
      print "NO MATCH"
   end = time.time()
   print "compare = " + str(end - start)
   
   file1.close()
   file2.close()
   exit(0)

def fftconvert(file):

   # store attributes of wav file
   (nchannels, sampwidth, framerate, nframes, comptype, compname) = file.getparams()
   
   start = time.time()
   # i don't really know yet
   frames = file.readframes (nframes * nchannels)
   end = time.time()
   print "readframe = " + str(end - start)
   
   start = time.time()
   # converts data in array somehow...research more
   out = struct.unpack_from ("%dh" % nframes * nchannels, frames)
   end = time.time()
   print "unpack = " + str(end - start)
   
   
   start = time.time() 
   # send the unpacked data through the fft
   # output is an array of complex numbers
   ffta = fftpack.fft(out)
   print ffta
   end = time.time()
   print "fft = " + str(end - start)
   
   # convert the values in the array retrieved from fft to freqeuncies
   freqs = numpy.fft.fftfreq(len(out))
   # print freqs
   
   
   # do we even need to convert the array into hertz?
   idx = numpy.argmax(numpy.abs(ffta)**2)
   freq = freqs[idx]
   # print freqs[15200]
   
   # convert the frequency to hertz
   hertz = abs(freq*framerate)
   # print hertz
   
   start = time.time()
   # convert each value in array to hertz
   x = 0
   while x < len(freqs):
      freqs[x] = abs(freqs[x] * framerate)
      x = x + 1
   print freqs
   end = time.time()
   print "Convert to Hz: " + str(end-start)
   
   # return the array of frequencies in hertz
   return freqs
    
   

match()
