#!/usr/bin/python

import sys
import time
import unittest
import imp

p4500 = imp.load_source("p4500", "../p4500")

class TestAllCombinations(unittest.TestCase):

    # 5 seconds subset
    def test_trouble_x1_match(self):
        self.assertTrue(p4500.match('../A4/trouble.wav', '../A4/x1.wav'))

    # 5 seconds subset with noise
    def test_trouble_x2_match(self):
        self.assertTrue(p4500.match('../A4/trouble.wav', '../A4/x2.wav'))

    # 5 seconds subset with noise and swapped channels
    def test_trouble_x3_match(self):
        self.assertTrue(p4500.match('../A4/trouble.wav', '../A4/x3.wav'))

    # 23.8 seconds subset
    def test_trouble_x4_match(self):
        self.assertTrue(p4500.match('../A4/trouble.wav', '../A4/x4.wav'))

    # 23.8 seconds subset with lower volume
    def test_trouble_x5_match(self):
        self.assertTrue(p4500.match('../A4/trouble.wav', '../A4/x5.wav'))

    # 23.8 seconds subset convert to mp3 and back to wav
    def test_trouble_x6_match(self):
        self.assertTrue(p4500.match('../A4/trouble.wav', '../A4/x6.wav'))

    # same file with noise
    def test_x1_x2_match(self):
        self.assertTrue(p4500.match('../A4/x1.wav', '../A4/x2.wav'))

    # same file with noise and swapped channels
    def test_x1_x3_match(self):
        self.assertTrue(p4500.match('../A4/x1.wav', '../A4/x3.wav'))

    # same file with swapped channels
    def test_x2_x3_match(self):
        self.assertTrue(p4500.match('../A4/x2.wav', '../A4/x3.wav'))

    # 22 seconds subset
    def test_wayfaring_x7_match(self):
        self.assertTrue(p4500.match('../A4/wayfaring.wav', '../A4/x7.wav'))

    # 22 seconds converted to mp3 and back to wav
    def test_wayfaring_x8_match(self):
        self.assertTrue(p4500.match('../A4/wayfaring.wav', '../A4/x8.wav'))

    # 22 seconds converted to mp3 and back to wav, added noise and swapped channels
    def test_wayfaring_x9_match(self):
        self.assertTrue(p4500.match('../A4/wayfaring.wav', '../A4/x9.wav'))

    # same file converted to mp3 and back to wav
    def test_x7_x8_match(self):
        self.assertTrue(p4500.match('../A4/x7.wav', '../A4/x8.wav'))

    # same file converted to mp3 and back to wav, added noise and swapped channels
    def test_x7_x9_match(self):
        self.assertTrue(p4500.match('../A4/x7.wav', '../A4/x9.wav'))

    # same file with added noise and swapped channels
    def test_x8_x9_match(self):
        self.assertTrue(p4500.match('../A4/x8.wav', '../A4/x9.wav')) 

    # 5 seconds subset
    def test_hewlett_x10_match(self):
        self.assertTrue(p4500.match('../A4/hewlett.wav', '../A4/x10.wav'))

    # 23.8 seconds subset
    def test_hewlett_x11_match(self):
        self.assertTrue(p4500.match('../A4/hewlett.wav', '../A4/x11.wav'))

    # 22 seconds subset
    def test_hewlett_x12_match(self):
        self.assertTrue(p4500.match('../A4/hewlett.wav', '../A4/x12.wav'))

    # 5 seconds subset
    def test_x10_x11_match(self):
        self.assertTrue(p4500.match('../A4/x10.wav', '../A4/x11.wav'))

if __name__ == '__main__':
    unittest.main()
