import pytest
from plates import *

def test_plates():
    assert is_valid("HELLO") == True
    assert is_valid("Hello") == True
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("GOODBYE") == False
    assert is_valid("goodbye") == False
    assert is_valid("") == False
    assert
