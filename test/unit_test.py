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

    def test_is_a_subset_match(self):
        self.assertTrue(p4500.match('../A4/trouble.wav', '../A4/x1.wav'))

    def test_is_a_subset_match2(self):
        self.assertTrue(p4500.match('../A4/trouble.wav', '../A4/x2.wav'))

    def test_is_a_subset_match3(self):
        self.assertTrue(p4500.match('../A4/trouble.wav', '../A4/x3.wav'))

    def test_is_a_subset_match4(self):
        self.assertTrue(p4500.match('../A4/trouble.wav', '../A4/x4.wav'))

    def test_is_a_subset_match5(self):
        self.assertTrue(p4500.match('../A4/trouble.wav', '../A4/x5.wav'))

    def test_is_a_subset_match6(self):
        self.assertTrue(p4500.match('../A4/trouble.wav', '../A4/x6.wav'))

    def test_is_a_subset_match7(self):
        self.assertTrue(p4500.match('../A4/wayfaring.wav', '../A4/x7.wav'))

    def test_is_a_subset_match8(self):
        self.assertTrue(p4500.match('../A4/wayfaring.wav', '../A4/x8.wav'))

    def test_is_a_subset_match9(self):
        self.assertTrue(p4500.match('../A4/wayfaring.wav', '../A4/x9.wav'))

    def test_is_a_subset_match10(self):
        self.assertTrue(p4500.match('../A4/hewlett.wav', '../A4/x10.wav'))

    def test_is_a_subset_match11(self):
        self.assertTrue(p4500.match('../A4/hewlett.wav', '../A4/x11.wav'))

    def test_is_a_subset_match12(self):
        self.assertTrue(p4500.match('../A4/hewlett.wav', '../A4/x12.wav'))

    def test_is_a_subset_match13(self):
        self.assertTrue(p4500.match('../A4/x11.wav', '../A4/x10.wav'))

    def test_non_wav_file_returns_error(self):
        with self.assertRaises(SystemExit):
            p4500.match('../A4/x1.wav', '../README')

if __name__ == '__main__':
    unittest.main()
