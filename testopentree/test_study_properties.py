#!/usr/bin/env python3
import unittest
from testopentree import run_example_script_or_skip as ex_runner

class TestExamples(unittest.TestCase):

    def test_study_properties(self):

        def res_checker(test_case, results):
            rd = results.response_dict
            test_case.assertTrue('tree_properties' in rd)
            test_case.assertTrue('study_properties' in rd)

        ex_runner(self, 'study_properties.py', [], res_checker)


if __name__ == '__main__':
    unittest.main()
