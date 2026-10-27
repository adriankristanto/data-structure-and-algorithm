import pytest

from contains_duplicate_217 import Solution


# parametrize asks pytest to run the same testing function on several different inputs
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([1], False),
        ([1, 1], True),
        ([-1, -2, -1], True),
        ([0, 0], True),
        ([5, 4, 3, 2, 1], False),
        ([7, 7, 7, 7], True),
    ],
)
def test_contains_duplicate_217(nums, expected):
    solution = Solution()
    result = solution.containsDuplicate(nums)
    assert result == expected
