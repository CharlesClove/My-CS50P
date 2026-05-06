from bank import value
import pytest

def test_value():
    @pytest.mark.parametrize("input, expected", [
    (2, 4),
    (3, 9),
    (4, 16),
    ])
