import os
import sys
sys.path.insert(1, os.path.abspath('.'))
from src import main

def test_inc():
    assert main.inc(3) == 4

def test_dec():
    assert main.dec(3) == 2