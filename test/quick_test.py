#!/usr/bin/python

import sys
import time
import unittest
import imp

p4500 = imp.load_source("p4500", "../p4500")

class QuickTest(unittest.TestCase):

    # same file with noise
    def test_x1_x2_match(self):
        self.assertTrue(p4500.match('../A4/x1.wav', '../A4/x2.wav'))

    # same file with noise and swapped channels
    def test_x1_x3_match(self):
        self.assertTrue(p4500.match('../A4/x1.wav', '../A4/x3.wav'))

    # same file with swapped channels
    def test_x2_x3_match(self):
        self.assertTrue(p4500.match('../A4/x2.wav', '../A4/x3.wav'))

    # same file converted to mp3 and back to wav
    def test_x7_x8_match(self):
        self.assertTrue(p4500.match('../A4/x7.wav', '../A4/x8.wav'))

    # same file converted to mp3 and back to wav, added noise and swapped channels
    def test_x7_x9_match(self):
        self.assertTrue(p4500.match('../A4/x7.wav', '../A4/x9.wav'))

    # 5 seconds subset
    def test_x10_x11_match(self):
        self.assertTrue(p4500.match('../A4/x10.wav', '../A4/x11.wav'))

    # no match tests:
    def test_x1_x4_no_match(self):
        self.assertFalse(p4500.match('../A4/x1.wav', '../A4/x4.wav'))

    def test_x1_x7_no_match(self):
        self.assertFalse(p4500.match('../A4/x1.wav', '../A4/x7.wav'))

    def test_x1_x10_no_match(self):
        self.assertFalse(p4500.match('../A4/x1.wav', '../A4/x10.wav'))

    def test_x1_x12_no_match(self):
        self.assertFalse(p4500.match('../A4/x1.wav', '../A4/x12.wav'))

    def test_x4_x7_no_match(self):
        self.assertFalse(p4500.match('../A4/x4.wav', '../A4/x7.wav'))

    def test_x4_x12_no_match(self):
        self.assertFalse(p4500.match('../A4/x4.wav', '../A4/x12.wav'))

    def test_x7_x11_no_match(self):
        self.assertFalse(p4500.match('../A4/x7.wav', '../A4/x11.wav'))

    def test_x10_x12_no_match(self):
        self.assertFalse(p4500.match('../A4/x10.wav', '../A4/x12.wav'))

    def test_x11_x12_no_match(self):
        self.assertFalse(p4500.match('../A4/x11.wav', '../A4/x12.wav'))


    # test for incorrect file format (txt)
    def test_non_wav_file_returns_error(self):
        with self.assertRaises(SystemExit):
            p4500.match('../A4/x1.wav', '../README')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(QuickTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
