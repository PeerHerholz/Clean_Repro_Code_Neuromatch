
import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]

@pytest.mark.sum
def test_sum(sample_data):
    assert sum(sample_data) == 15
