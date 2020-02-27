#!/usr/bin/env python3
import unittest
from testopentree import run_example_script_or_skip as ex_runner

class TestExamples(unittest.TestCase):
    def test_about_example(self):
        ex_runner(self, 'about.py', None)


if __name__ == '__main__':
    unittest.main()
