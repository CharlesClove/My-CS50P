from bank import value
import pytest

def test_hello():
    assert value("hello") == '$0'
    assert value("Hello") == '$0'
#def test_h():
    assert value("hey,") == '$20'
    assert value("Hola,") == '$20'
#def test_else():
    assert value("What's up") == '$100'
