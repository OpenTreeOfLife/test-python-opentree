#!/usr/bin/env python3
import unittest
from testopentree import run_example_script_or_skip as ex_runner

class TestExamples(unittest.TestCase):

    def test_tnrs_infer_contexts(self):
        res = {"ambiguous_names": [],
               "context_name": "Mammals",
               "context_ott_id": 244265,
              }
        def res_checker(test_case, results):
            test_case.assertEqual(res, results.response_dict)

        args = ['Pan', 'Homo']
        ex_runner(self, 'tnrs_infer_contexts.py', args, res_checker)


if __name__ == '__main__':
    unittest.main()
