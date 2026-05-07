import pytest
from fuel import *

def test_gague():
    assert gauge(99) == "F"
    assert gauge(0) == "E"
    assert gauge(25) == "25%"
    with pytest.raises(ValueError):
        convert("cat/dog")
        convert("-1/100")
        convert("25/0")
    # with pytest.raises(ZeroDivisionError):
        convert("25/0")
