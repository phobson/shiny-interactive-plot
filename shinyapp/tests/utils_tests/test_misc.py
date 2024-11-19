import pytest

from utils.misc import add_numbers


@pytest.mark.parametrize(
    ("x", "y", "expected"),
    [
        [1, 1, 2],
        [2, 6, 8],
    ],
)
def test_add_numbers(x, y, expected):
    assert add_numbers(x, y) == expected
