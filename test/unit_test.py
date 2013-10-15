#!/usr/bin/python

import sys
import time
import unittest

sys.path.append('../')
import audio_match as p4500

class TestBasics(unittest.TestCase):
	
	def test_is_a_self_match(self):
		self.assertTrue(p4500.match('../A4/x1.wav', '../A4/x1.wav'))

	def test_is_not_a_match(self):
		self.assertFalse(p4500.match('../A4/x1.wav', '../A4/x10.wav'))

if __name__ == '__main__':
	unittest.main()