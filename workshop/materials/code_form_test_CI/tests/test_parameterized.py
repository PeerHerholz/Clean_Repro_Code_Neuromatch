
import pytest

@pytest.mark.parametrize("a,b,expected", [(1, 1, 2), (2, 3, 5), (3, 3, 6)])
def test_addition(a, b, expected):
    assert a + b == expected
