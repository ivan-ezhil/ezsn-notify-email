import pytest


def add(a, b):
    return a + b


def test_add_numbers():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (10, 20, 30),
    (-1, -1, -2),
    (0, 0, 0),
])
def test_add_multiple(a, b, expected):
    assert add(a, b) == expected
