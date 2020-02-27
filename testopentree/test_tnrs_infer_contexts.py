#!/usr/bin/env python3
import unittest
from testopentree import run_example_script_or_skip as ex_runner

class TestExamples(unittest.TestCase):
    def test_tnrs_match_example(self):
        args = ['Characidiopsis acuta']
        ex_runner(self, 'tnrs_match_names.py', args)


if __name__ == '__main__':
    unittest.main()
