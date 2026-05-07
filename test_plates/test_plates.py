import pytest
from plates import *

def test_plates():
    assert is_valid("HELLO") == True
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("GOODBYE") == False
    assert is_valid("goodbye") == False
    assert is_valid("222222") == False
    assert is_valid(" AAAAA") == False
    assert is_valid("000000") == False
