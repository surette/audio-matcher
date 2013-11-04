#!/usr/bin/python

import sys
import time
import unittest
import imp

p4500 = imp.load_source("p4500", "../p4500")

class NoMatchTests(unittest.TestCase):

    # no match tests:
    # trouble vs all
    def test_trouble_wayfaring_no_match(self):
        self.assertFalse(p4500.match('../A4/trouble.wav', '../A4/wayfaring.wav'))

    def test_trouble_hewlett_no_match(self):
        self.assertFalse(p4500.match('../A4/trouble.wav', '../A4/hewlett.wav'))

    def test_trouble_x7_no_match(self):
        self.assertFalse(p4500.match('../A4/trouble.wav', '../A4/x7.wav'))

    def test_trouble_x8_no_match(self):
        self.assertFalse(p4500.match('../A4/trouble.wav', '../A4/x8.wav'))

    def test_trouble_x9_no_match(self):
        self.assertFalse(p4500.match('../A4/trouble.wav', '../A4/x9.wav'))

    def test_trouble_x10_no_match(self):
        self.assertFalse(p4500.match('../A4/trouble.wav', '../A4/x10.wav'))

    def test_trouble_x11_no_match(self):
        self.assertFalse(p4500.match('../A4/trouble.wav', '../A4/x11.wav'))

    def test_trouble_x12_no_match(self):
        self.assertFalse(p4500.match('../A4/trouble.wav', '../A4/x12.wav'))

    # wayfaring vs all
    def test_wayfaring_hewlett_no_match(self):
        self.assertFalse(p4500.match('../A4/wayfaring.wav', '../A4/hewlett.wav'))

    def test_wayfaring_x1_no_match(self):
        self.assertFalse(p4500.match('../A4/wayfaring.wav', '../A4/x1.wav'))

    def test_wayfaring_x2_no_match(self):
        self.assertFalse(p4500.match('../A4/wayfaring.wav', '../A4/x2.wav'))

    def test_wayfaring_x3_no_match(self):
        self.assertFalse(p4500.match('../A4/wayfaring.wav', '../A4/x3.wav'))

    def test_wayfaring_x4_no_match(self):
        self.assertFalse(p4500.match('../A4/wayfaring.wav', '../A4/x4.wav'))

    def test_wayfaring_x5_no_match(self):
        self.assertFalse(p4500.match('../A4/wayfaring.wav', '../A4/x5.wav'))

    def test_wayfaring_x6_no_match(self):
        self.assertFalse(p4500.match('../A4/wayfaring.wav', '../A4/x6.wav'))

    def test_wayfaring_x10_no_match(self):
        self.assertFalse(p4500.match('../A4/wayfaring.wav', '../A4/x10.wav'))

    def test_wayfaring_x11_no_match(self):
        self.assertFalse(p4500.match('../A4/wayfaring.wav', '../A4/x11.wav'))

    def test_wayfaring_x12_no_match(self):
        self.assertFalse(p4500.match('../A4/wayfaring.wav', '../A4/x12.wav'))

    # hewlett vs all
    def test_hewlett_x1_no_match(self):
        self.assertFalse(p4500.match('../A4/hewlett.wav', '../A4/x1.wav'))

    def test_hewlett_x2_no_match(self):
        self.assertFalse(p4500.match('../A4/hewlett.wav', '../A4/x2.wav'))

    def test_hewlett_x3_no_match(self):
        self.assertFalse(p4500.match('../A4/hewlett.wav', '../A4/x3.wav'))

    def test_hewlett_x4_no_match(self):
        self.assertFalse(p4500.match('../A4/hewlett.wav', '../A4/x4.wav'))

    def test_hewlett_x5_no_match(self):
        self.assertFalse(p4500.match('../A4/hewlett.wav', '../A4/x5.wav'))

    def test_hewlett_x6_no_match(self):
        self.assertFalse(p4500.match('../A4/hewlett.wav', '../A4/x6.wav'))

    def test_hewlett_x7_no_match(self):
        self.assertFalse(p4500.match('../A4/hewlett.wav', '../A4/x7.wav'))

    def test_hewlett_x8_no_match(self):
        self.assertFalse(p4500.match('../A4/hewlett.wav', '../A4/x8.wav'))

    def test_hewlett_x9_no_match(self):
        self.assertFalse(p4500.match('../A4/hewlett.wav', '../A4/x9.wav'))

    # x1 vs all
    def test_x1_x4_no_match(self):
        self.assertFalse(p4500.match('../A4/x1.wav', '../A4/x4.wav'))

    def test_x1_x5_no_match(self):
        self.assertFalse(p4500.match('../A4/x1.wav', '../A4/x5.wav'))

    def test_x1_x6_no_match(self):
        self.assertFalse(p4500.match('../A4/x1.wav', '../A4/x6.wav'))

    def test_x1_x7_no_match(self):
        self.assertFalse(p4500.match('../A4/x1.wav', '../A4/x7.wav'))

    def test_x1_x8_no_match(self):
        self.assertFalse(p4500.match('../A4/x1.wav', '../A4/x8.wav'))

    def test_x1_x9_no_match(self):
        self.assertFalse(p4500.match('../A4/x1.wav', '../A4/x9.wav'))

    def test_x1_x10_no_match(self):
        self.assertFalse(p4500.match('../A4/x1.wav', '../A4/x10.wav'))

    def test_x1_x11_no_match(self):
        self.assertFalse(p4500.match('../A4/x1.wav', '../A4/x11.wav'))

    def test_x1_x12_no_match(self):
        self.assertFalse(p4500.match('../A4/x1.wav', '../A4/x12.wav'))

    # x2 vs all
    def test_x2_x4_no_match(self):
        self.assertFalse(p4500.match('../A4/x2.wav', '../A4/x4.wav'))

    def test_x2_x5_no_match(self):
        self.assertFalse(p4500.match('../A4/x2.wav', '../A4/x5.wav'))

    def test_x2_x6_no_match(self):
        self.assertFalse(p4500.match('../A4/x2.wav', '../A4/x6.wav'))

    def test_x2_x7_no_match(self):
        self.assertFalse(p4500.match('../A4/x2.wav', '../A4/x7.wav'))

    def test_x2_x8_no_match(self):
        self.assertFalse(p4500.match('../A4/x2.wav', '../A4/x8.wav'))

    def test_x2_x9_no_match(self):
        self.assertFalse(p4500.match('../A4/x2.wav', '../A4/x9.wav'))

    def test_x2_x10_no_match(self):
        self.assertFalse(p4500.match('../A4/x2.wav', '../A4/x10.wav'))

    def test_x2_x11_no_match(self):
        self.assertFalse(p4500.match('../A4/x2.wav', '../A4/x11.wav'))

    def test_x2_x12_no_match(self):
        self.assertFalse(p4500.match('../A4/x2.wav', '../A4/x12.wav'))

    # x3 vs all
    def test_x3_x4_no_match(self):
        self.assertFalse(p4500.match('../A4/x3.wav', '../A4/x4.wav'))

    def test_x3_x5_no_match(self):
        self.assertFalse(p4500.match('../A4/x3.wav', '../A4/x5.wav'))

    def test_x3_x6_no_match(self):
        self.assertFalse(p4500.match('../A4/x3.wav', '../A4/x6.wav'))

    def test_x3_x7_no_match(self):
        self.assertFalse(p4500.match('../A4/x3.wav', '../A4/x7.wav'))

    def test_x3_x8_no_match(self):
        self.assertFalse(p4500.match('../A4/x3.wav', '../A4/x8.wav'))

    def test_x3_x9_no_match(self):
        self.assertFalse(p4500.match('../A4/x3.wav', '../A4/x9.wav'))

    def test_x3_x10_no_match(self):
        self.assertFalse(p4500.match('../A4/x3.wav', '../A4/x10.wav'))

    def test_x3_x11_no_match(self):
        self.assertFalse(p4500.match('../A4/x3.wav', '../A4/x11.wav'))

    def test_x3_x12_no_match(self):
        self.assertFalse(p4500.match('../A4/x3.wav', '../A4/x12.wav'))

    # x4 vs all
    def test_x4_x7_no_match(self):
        self.assertFalse(p4500.match('../A4/x4.wav', '../A4/x7.wav'))

    def test_x4_x8_no_match(self):
        self.assertFalse(p4500.match('../A4/x4.wav', '../A4/x8.wav'))

    def test_x4_x9_no_match(self):
        self.assertFalse(p4500.match('../A4/x4.wav', '../A4/x9.wav'))

    def test_x4_x10_no_match(self):
        self.assertFalse(p4500.match('../A4/x4.wav', '../A4/x10.wav'))

    def test_x4_x11_no_match(self):
        self.assertFalse(p4500.match('../A4/x4.wav', '../A4/x11.wav'))

    def test_x4_x12_no_match(self):
        self.assertFalse(p4500.match('../A4/x4.wav', '../A4/x12.wav'))

    # x5 vs all
    def test_x5_x7_no_match(self):
        self.assertFalse(p4500.match('../A4/x5.wav', '../A4/x7.wav'))

    def test_x5_x8_no_match(self):
        self.assertFalse(p4500.match('../A4/x5.wav', '../A4/x8.wav'))

    def test_x5_x9_no_match(self):
        self.assertFalse(p4500.match('../A4/x5.wav', '../A4/x9.wav'))

    def test_x5_x10_no_match(self):
        self.assertFalse(p4500.match('../A4/x5.wav', '../A4/x10.wav'))

    def test_x5_x11_no_match(self):
        self.assertFalse(p4500.match('../A4/x5.wav', '../A4/x11.wav'))

    def test_x5_x12_no_match(self):
        self.assertFalse(p4500.match('../A4/x5.wav', '../A4/x12.wav'))
    

    # x6 vs all
    def test_x6_x7_no_match(self):
        self.assertFalse(p4500.match('../A4/x6.wav', '../A4/x7.wav'))

    def test_x6_x8_no_match(self):
        self.assertFalse(p4500.match('../A4/x6.wav', '../A4/x8.wav'))

    def test_x6_x9_no_match(self):
        self.assertFalse(p4500.match('../A4/x6.wav', '../A4/x9.wav'))

    def test_x6_x10_no_match(self):
        self.assertFalse(p4500.match('../A4/x6.wav', '../A4/x10.wav'))

    def test_x6_x11_no_match(self):
        self.assertFalse(p4500.match('../A4/x6.wav', '../A4/x11.wav'))

    def test_x6_x12_no_match(self):
        self.assertFalse(p4500.match('../A4/x6.wav', '../A4/x12.wav'))


    # x7 vs all
    def test_x7_x10_no_match(self):
        self.assertFalse(p4500.match('../A4/x7.wav', '../A4/x10.wav'))

    def test_x7_x11_no_match(self):
        self.assertFalse(p4500.match('../A4/x7.wav', '../A4/x11.wav'))

    def test_x7_x12_no_match(self):
        self.assertFalse(p4500.match('../A4/x7.wav', '../A4/x12.wav'))


    # x8 vs all
    def test_x8_x10_no_match(self):
        self.assertFalse(p4500.match('../A4/x8.wav', '../A4/x10.wav'))

    def test_x8_x11_no_match(self):
        self.assertFalse(p4500.match('../A4/x8.wav', '../A4/x11.wav'))

    def test_x8_x12_no_match(self):
        self.assertFalse(p4500.match('../A4/x8.wav', '../A4/x12.wav'))


    # x9 vs all
    def test_x9_x10_no_match(self):
        self.assertFalse(p4500.match('../A4/x9.wav', '../A4/x10.wav'))

    def test_x9_x11_no_match(self):
        self.assertFalse(p4500.match('../A4/x9.wav', '../A4/x11.wav'))

    def test_x9_x12_no_match(self):
        self.assertFalse(p4500.match('../A4/x9.wav', '../A4/x12.wav'))


    # x12 vs all
    def test_x10_x12_no_match(self):
        self.assertFalse(p4500.match('../A4/x10.wav', '../A4/x12.wav'))

    def test_x11_x12_no_match(self):
        self.assertFalse(p4500.match('../A4/x11.wav', '../A4/x12.wav'))


    # test for incorrect file format (txt)
    def test_non_wav_file_returns_error(self):
        with self.assertRaises(SystemExit):
            p4500.match('../A4/x1.wav', '../README')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(NoMatchTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
