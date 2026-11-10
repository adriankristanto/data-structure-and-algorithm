import pytest

from longest_consecutive_sequence_128 import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([1, 0, 1, 2], 3),
        ([], 0),
        ([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], 11),
        ([1, 2, 6, 7, 8], 3),
        ([0], 1),
    ],
)
def test_longest_consecutive_sequence_128(nums: list[int], expected: int):
    solution = Solution()
    result = solution.longestConsecutive(nums)
    assert result == expected
