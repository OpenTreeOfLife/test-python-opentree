#!/usr/bin/env python3
import unittest
from testopentree import run_example_script_or_skip as ex_runner

class TestExamples(unittest.TestCase):

    def test_synth_induced_subtree(self):

        def res_checker(test_case, results):
            tree = results.tree
            tn = tree.taxon_namespace
            for taxon in tn:
                if taxon.label != 'mrcaott246ott1566':
                    test_case.assertEqual(199350, taxon.ott_id)

        args = ['--ott-ids=199350', '--node-ids=mrcaott246ott1566'] # ott733093']
        ex_runner(self, 'synth_induced_subtree.py', args, res_checker)


if __name__ == '__main__':
    unittest.main()
