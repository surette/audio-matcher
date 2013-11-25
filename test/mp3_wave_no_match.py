#!/usr/bin/python

import sys
import time
import unittest
import imp

p4500 = imp.load_source("p4500", "../p4500")

class ShortNoMatchTests(unittest.TestCase):
    # x1 vs all
    def test_x1_x4_no_match(self):
        self.assertFalse(p4500.match('../A4/x1.wav', '../A4/x4.mp3'))

    def test_x1_x8_no_match(self):
        self.assertFalse(p4500.match('../A4/x1.mp3', '../A4/x8.wav'))

    def test_x1_x9_no_match(self):
        self.assertFalse(p4500.match('../A4/x1.wav', '../A4/x9.mp3'))

    def test_x1_x10_no_match(self):
        self.assertFalse(p4500.match('../A4/x1.wav', '../A4/x10.wav'))

    def test_x1_x11_no_match(self):
        self.assertFalse(p4500.match('../A4/x1.wav', '../A4/x11.mp3'))

    def test_x1_x12_no_match(self):
        self.assertFalse(p4500.match('../A4/x1.mp3', '../A4/x12.wav'))

    # x2 vs all
    def test_x2_x4_no_match(self):
        self.assertFalse(p4500.match('../A4/x2.mp3', '../A4/x4.wav'))

    def test_x2_x5_no_match(self):
        self.assertFalse(p4500.match('../A4/x2.wav', '../A4/x5.mp3'))

    def test_x2_x6_no_match(self):
        self.assertFalse(p4500.match('../A4/x2.mp3', '../A4/x6.wav'))

    def test_x2_x7_no_match(self):
        self.assertFalse(p4500.match('../A4/x2.mp3', '../A4/x7.wav'))

    def test_x2_x8_no_match(self):
        self.assertFalse(p4500.match('../A4/x2.wav', '../A4/x8.mp3'))

    # x3 vs all
    def test_x3_x4_no_match(self):
        self.assertFalse(p4500.match('../A4/x3.mp3', '../A4/x4.wav'))

    def test_x3_x5_no_match(self):
        self.assertFalse(p4500.match('../A4/x3.wav', '../A4/x5.mp3'))

    def test_x3_x6_no_match(self):
        self.assertFalse(p4500.match('../A4/x3.wav', '../A4/x6.mp3'))

    def test_x3_x7_no_match(self):
        self.assertFalse(p4500.match('../A4/x3.mp3', '../A4/x7.wav'))

    # x4 vs all
    def test_x4_x7_no_match(self):
        self.assertFalse(p4500.match('../A4/x4.wav', '../A4/x7.mp3'))

    def test_x4_x8_no_match(self):
        self.assertFalse(p4500.match('../A4/x4.mp3', '../A4/x8.wav'))

    def test_x4_x9_no_match(self):
        self.assertFalse(p4500.match('../A4/x4.wav', '../A4/x9.mp3'))

    def test_x4_x10_no_match(self):
        self.assertFalse(p4500.match('../A4/x4.mp3', '../A4/x10.wav'))

    def test_x5_x11_no_match(self):
        self.assertFalse(p4500.match('../A4/x5.wav', '../A4/x11.mp3'))

    def test_x5_x12_no_match(self):
        self.assertFalse(p4500.match('../A4/x5.mp3', '../A4/x12.wav'))

    # x12 vs all
    def test_x10_x12_no_match(self):
        self.assertFalse(p4500.match('../A4/x10.wav', '../A4/x12.mp3'))

    def test_x11_x12_no_match(self):
        self.assertFalse(p4500.match('../A4/x11.mp3', '../A4/x12.wav'))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ShortNoMatchTests)
    unittest.TextTestRunner(verbosity=2).run(suite)