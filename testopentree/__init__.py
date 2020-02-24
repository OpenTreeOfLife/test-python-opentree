#!/usr/bin/env python3

import os
import logging


_PODIR, _EXAMPLES_DIR = None, None
_CHECKED_POD, _CHECKED_EXAMPLES = False, False
def get_python_opendir_top():
    global _PODIR, _CHECKED_POD
    if _PODIR is None:
        if _CHECKED_POD:
            return None
        pod = os.environ.get('PYTHON_OPENTREE_DIR')
        _CHECKED_POD = True
        if pod is None:
            logging.warning('PYTHON_OPENTREE_DIR environmental variable is not set.')
        elif not os.path.isdir(pod):
            logging.warning('PYTHON_OPENTREE_DIR value "{}" is not a readable directory.'.format(pod))
        else:
            _PODIR = pod
    return _PODIR

def get_python_opendir_examples():
    global _EXAMPLES_DIR, _CHECKED_EXAMPLES
    if _EXAMPLES_DIR is None:
        if _CHECKED_EXAMPLES:
            return None
        _CHECKED_EXAMPLES = True
        pod = get_python_opendir_top()
        if pod is None:
            return None
        ed = os.path.join(pod, 'examples')
        if not os.path.isdir(ed):
            logging.warning('"{}" is not a readable directory.'.format(ed))
        else:
            _EXAMPLES_DIR = ed
    return _EXAMPLES_DIR

def get_example_script_or_skip(test_case, file_name):
    ed = get_python_opendir_examples()
    if ed is None:
        test_case.skipTest('PYTHON_OPENTREE_DIR is not set or does not exist')
        return None
    tes = os.path.join(ed, file_name)
    if not os.path.isfile(tes):
        test_case.skipTest('"{}" is not a readable file'.format(tes))
        return None
    return tes

def run_example_script_or_skip(test_case, file_name, arg_list, res_checker=None):
    # See https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
    filepath = get_example_script_or_skip(test_case, file_name)
    if filepath is None:
        return None
    import importlib.util
    mn = 'opentreeexample{}'.format(file_name.split('.')[0])
    spec = importlib.util.spec_from_file_location(mn, filepath)
    tmp_mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tmp_mod)
    if arg_list is None:
        arg_list = []
    lfr = None if res_checker is None else []
    rc = tmp_mod.main(arg_list, out=None, list_for_results=lfr)
    if res_checker is not None:
        res_checker(test_case, lfr[0])
    return rc