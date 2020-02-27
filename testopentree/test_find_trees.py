#!/usr/bin/env python3
import unittest
from testopentree import run_example_script_or_skip as ex_runner

class TestExamples(unittest.TestCase):

    def test_find_trees(self):
        obj = {
            "matched_trees": [
                {"ot:studyId": "pg_719", "ot:treeId": "tree1294"},
                {"ot:studyId": "pg_719", "ot:treeId": "tree1295"},
                {"ot:studyId": "pg_719", "ot:treeId": "tree1296"}
            ],
            "ot:studyId": "pg_719"
            }
        res = {"matched_studies": [obj]}

        def res_checker(test_case, results):
            test_case.assertEqual(res, results.response_dict)

        args = ['--property=ot:studyId', 'pg_719']
        ex_runner(self, 'find_trees.py', args, res_checker)


if __name__ == '__main__':
    unittest.main()
