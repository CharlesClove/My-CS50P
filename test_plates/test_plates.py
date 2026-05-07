import pytest
from plates import *

def test_plates():
    assert is_valid("AA") == True
    assert is_valid("A2") == False

    assert is_valid("2A") == False
    assert is_valid("22") == False
    assert is_valid(" 2") == False
