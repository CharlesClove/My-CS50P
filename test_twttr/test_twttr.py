import pytest
from twttr import *

def test_shorten():
    assert shorten("twitter") == "twttr"
