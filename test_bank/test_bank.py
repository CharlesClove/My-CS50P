from bank import value
import pytest

def test_bank():
    assert value("hello") == '$0'
    assert value("Hello") == '$0'
    assert value("Hello") == '$20'
    assert value("hey,") == '$20'
    assert value("Hola,") == '$20'
    assert value("What's up") == '$100'
