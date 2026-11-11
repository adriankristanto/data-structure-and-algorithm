import pytest

from valid_parentheses_20 import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("([)]", False),
        ("]", False),
    ],
)
def test_valid_parentheses_20(s, expected):
    solution = Solution()
    result = solution.isValid(s)
    assert result == expected
