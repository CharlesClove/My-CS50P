import pytest
from twttr import *

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("123") == "123"
    assert shorten("a,b,c") == ",b,c"
def test_shorten_fail():
    assert shorten("twitter") == "twitter"
    assert shorten("123") == "123"
    assert shorten("a,b,c") == "a,b,c"
