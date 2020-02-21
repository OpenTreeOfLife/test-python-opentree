test-python-opentree
====================

Optional more extensive tests of [python-opentree](https://opentree.readthedocs.io/en/latest/readme.html)


Usage:

  1. Set a PYTHON_OPENTREE_DIR to refer to the top of your local copy of the python-opentree 
    repository
    
  2. Using the same virtualenv that you installed python-opentree in:

    python setup.py develop

  3. from the top of the PYTHON_OPENTREE_DIR you can run pytest. For instance if you have the
    directories next to each other in the same directory then you can run:
    
    PYTHON_OPENTREE_DIR=$PWD pytest . ../test-python-opentree
 
 or 
    
    PYTHON_OPENTREE_DIR=$PWD coverage run -m pytest . ../test-python-opentree
 
 ## motivation
 This testing repo is intended for running slower tests. It uses some tricks to do things
 like load the examples scripts as modules. This is done to make it possible to get coverage
 statistics from all of the tests (by avoiding spawning new processes).