import pytest

from valid_anagram_214 import Solution


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("astronomer", "moon starer", True),
        ("", "", True),
        ("Silent", "Listen", True),
    ],
)
def test_valid_anagram_214(s, t, expected):
    solution = Solution()
    result = solution.isAnagram(s, t)
    assert result == expected
