import pytest
from twttr import *

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("123") == "123"
    assert shorten("a,b,c") == ",b,c"
    assert shorten("Ohh") == "hh"
