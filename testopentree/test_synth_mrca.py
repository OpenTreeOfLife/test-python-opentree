#!/usr/bin/env python3
import unittest
from testopentree import run_example_script_or_skip as ex_runner

class TestExamples(unittest.TestCase):

    def test_synth_mrca(self):
        args = ['--ott-ids=199350', '--node-ids=mrcaott246ott1566']
        ex_runner(self, 'synth_mrca.py', args, None)


if __name__ == '__main__':
    unittest.main()
