#!/usr/bin/python

import sys
import os
import time
import unittest

# dir = os.path.dirname(__file__)
# filename = os.path.join(dir, '../')
# print filename
sys.path.append('../')
import audio_match as p4500

class TestBasics(unittest.TestCase):
	
	def test_is_a_self_match(self):
		self.assertTrue(p4500.match('../A4/x1.wav', '../A4/x1.wav'))

	def test_matches_a_simple_subset(self):
		self.assertTrue(p4500.match('../A4/trouble.wav', '../A4/x1.wav'))

	def test_matches_altered_subsets(self):
		self.assertTrue(p4500.match('../A4/trouble.wav', '../A4/x2.wav'))

	def test_is_not_a_match(self):
		self.assertFalse(p4500.match('../A4/x1.wav', '../A4/x10.wav'))

if __name__ == '__main__':
	unittest.main()