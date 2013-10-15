#!/usr/bin/python

import sys
import time
import unittest

sys.path.append('../')
import fft_test2

class TestBasics(unittest.TestCase):
	
	def test_is_a_self_match(self):
		self.assertTrue(fft_test2.match('../A4/x1.wav', '../A4/x1.wav'))

	def test_is_not_a_match(self):
		self.assertFalse(fft_test2.match('../A4/x1.wav', '../A4/x10.wav'))

if __name__ == '__main__':
	unittest.main()