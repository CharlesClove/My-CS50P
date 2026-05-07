import pytest
from plates import *

def test_plates():
    assert is_valid() == True
    assert is_valid() == False
    assert is_valid() == False
