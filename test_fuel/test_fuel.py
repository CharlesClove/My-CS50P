import pytest
from fuel import *

def test_gague():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(25) == "25%"
    assert convert("25/100") == 25

def test_valueErrors():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("-1/100")
    with pytest.raises(ValueError):
        convert("10/-100")
    with pytest.raises(ValueError):
        convert("-10/-100")
    with pytest.raises(ValueError):
        convert("10/5")

def test_zeroDivision():
    with pytest.raises(ZeroDivisionError):
        convert("25/0")
