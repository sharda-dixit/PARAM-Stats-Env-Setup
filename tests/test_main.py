import os, sys
#sys.path.insert(1, os.path.abspath('.'))
sys.path.insert(1, os.getcwd())

from src import main

def test_inc():
    """A test fucntion for inc
    """    
    assert main.inc(3) == 4

def test_dec():
    """A test function for dec
    """    
    assert main.dec(3) == 2
