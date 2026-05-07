import pytest
from fuel import *

def test_gague():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(25) == "25%"
    assert convert("25/100") == 25
    with pytest.raises(ValueError):
        convert("cat/dog")
        convert("-1/100")
        convert("10/-100")
        convert("-10/-100")
        convert("10/5")
    with pytest.raises(ZeroDivisionError):
        convert("25/0")
