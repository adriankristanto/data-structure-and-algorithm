import pytest

from valid_palindrome_25 import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("A man, a plan, a canal: Panama", True),
        ("", True),
        (" ", True),
        ("Race car", True),
        ("Race a car", False),
        ("0P0", True),
        ("0P", False),
        ("a", True),
    ],
)
def test_valid_palindrome(s, expected):
    solution = Solution()
    result = solution.isPalindrome(s)
    assert result == expected
