#!/usr/bin/python

import sys
import time
import unittest
import imp

p4500 = imp.load_source("p4500", "../p4500")

class ErrorTest(unittest.TestCase):

    # test for incorrect file format (txt)
    def test_non_wav_file_returns_error(self):
        with self.assertRaises(SystemExit):
            p4500.match('../A4/x1.wav', '../README')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ErrorTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
