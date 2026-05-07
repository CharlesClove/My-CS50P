import pytest
from fuel import *

def test_gague():
    assert gauge(99) == "F"
    assert gauge(0) == "E"
    assert gauge(25) == "25%"
    assert convert("cat/dog") == 
