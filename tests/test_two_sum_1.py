import pytest

from two_sum_1 import Solution


def all_different(nums: list[int]) -> bool:
    return len(nums) == len(set(nums))


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]), 
        ([3, 2, 4], 6, [1, 2]), 
        ([3, 3], 6, [0, 1]) ,
        ([3, 3, 4, 5], 9, [2, 3])
    ] 
)
def test_two_sum(nums, target, expected):
    solution = Solution()
    result = solution.twoSum(nums, target)
    assert all_different(result), f"result contains duplicate(s): {result}"
    assert result == expected


@pytest.mark.parametrize(
    "nums, target",
    [
        ([], 10),
        ([5], 10),
        ([1, 2, 3], 10)
    ]
)
def test_two_sum_no_solution(nums, target):
    with pytest.raises(ValueError):
        Solution.twoSum(nums, target)