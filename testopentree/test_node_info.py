#!/usr/bin/env python3
import unittest
from testopentree import run_example_script_or_skip as ex_runner

class TestExamples(unittest.TestCase):

    def test_synth_induced_subtree(self):

        def res_checker(test_case, results):
            nd_ref = results.node_ref
            nd_id = nd_ref.node_id
            test_case.assertTrue(nd_id == 'ott189136' or nd_id.startswith('mrca'))

        args = ['--ott-ids=189136', '--include-lineage']
        ex_runner(self, 'synth_node_info.py', args, res_checker)


if __name__ == '__main__':
    unittest.main()
