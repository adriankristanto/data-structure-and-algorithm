import pytest
import json

from three_sum_15 import Solution, BruteForceSolution


@pytest.mark.parametrize(
    "numbers",
    [
        ([-1, 0, 1, 2, -1, -4]),
        ([0, 1, 1]),
        ([0, 0, 0]),
        ([1, 5]),
        ([]),
        ([0, 0, 0, 0, 0]),
        ([-1, 2, -1, 5, -4, 7, -6]),
    ],
    ids=[
        "general-1",
        "no-valid-triplets-1",
        "all-identicals-1",
        "invalid-input-size-1",
        "invalid-input-size-2",
        "all-identicals-2",
        "multiple-valid-triplets-same-fixed-value-1",
    ],
)
def test_brute_force_solution(numbers):
    bruteForceSolution = BruteForceSolution()
    solution = Solution()
    correct = bruteForceSolution.threeSum(numbers)
    result = solution.threeSum(numbers)
    assert sorted(correct) == sorted(result)
