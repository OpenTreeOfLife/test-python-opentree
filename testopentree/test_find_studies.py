#!/usr/bin/env python3
import unittest
from testopentree import run_example_script_or_skip as ex_runner

class TestExamples(unittest.TestCase):

    def test_find_studies(self):
        res = {"matched_studies": [{"ot:studyId": "pg_719"}]}
        def res_checker(test_case, results):
            test_case.assertEqual(res, results.response_dict)

        args = ['--property=ot:studyId', 'pg_719']
        ex_runner(self, 'find_studies.py', args, res_checker)


if __name__ == '__main__':
    unittest.main()
