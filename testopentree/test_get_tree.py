#!/usr/bin/env python3
import unittest
from testopentree import run_example_script_or_skip as ex_runner

class TestExamples(unittest.TestCase):

    def test_get_tree(self):
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
            tree = results.tree
            tn = tree.taxon_namespace
            test_case.assertTrue(str(results.tree).startswith('('))

        args = ['ot_1877', 'tree3', '--format=object']
        ex_runner(self, 'get_tree.py', args, res_checker)


if __name__ == '__main__':
    unittest.main()
