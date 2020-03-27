#!/usr/bin/env python3
import unittest
from testopentree import run_example_script_or_skip as ex_runner

class TestExamples(unittest.TestCase):

    def test_synth_subtree(self):

        def res_checker(test_case, results):
            taxon = results.taxon
            test_case.assertEqual(taxon.ott_id, 437610)
            test_case.assertTrue(len(taxon.lineage) > 0)
            
        args = ['--ott-id=437610']
        ex_runner(self, 'taxon_info.py', args, res_checker)


if __name__ == '__main__':
    unittest.main()
