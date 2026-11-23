import pytest

from two_sum_ii_input_array_is_sorted_167 import Solution, BruteForceSolution


@pytest.mark.parametrize(
    "numbers, target",
    [
        ([1, 2, 7, 11, 15], 9),
        ([0, 2, 3, 4, 5], 6),
        ([2, 3, 4], 7),
        ([0, 0], 0),
        ([-1, 0], -1),
        ([-2, 0, 2], 0),
    ],
)
def test_two_sum_ii_input_array_is_sorted_167(numbers, target):
    solution = Solution()
    result = solution.twoSum(numbers, target)
    bruteForceSolution = BruteForceSolution()
    correct = bruteForceSolution.twoSum(numbers, target)
    assert result == correct
