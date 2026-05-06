from bank import value
import pytest

def test_value():
    assert value("hello,") == '$0'
    assert value("hey,") == '$20'
    assert value("hola,") == '$20'
    assert value("I want a loan") == '$100'
