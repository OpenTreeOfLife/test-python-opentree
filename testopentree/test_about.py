#!/usr/bin/env python3
import unittest
from testopentree import run_example_script_or_skip

class TestAbout(unittest.TestCase):
    def test_about_example(self):
        run_example_script_or_skip(self, 'about.py', None)


    
if __name__ == '__main__':
    unittest.main()
