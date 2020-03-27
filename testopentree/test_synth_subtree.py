#!/usr/bin/env python3
import unittest
from testopentree import run_example_script_or_skip as ex_runner

class TestExamples(unittest.TestCase):

    def test_synth_subtree(self):

        def res_checker(test_case, results):
            tree = results.tree
            test_case.assertEqual(tree.seed_node.taxon.ott_id, 803675)

        args = ['--ott-id=803675']
        ex_runner(self, 'synth_subtree.py', args, res_checker)


if __name__ == '__main__':
    unittest.main()
