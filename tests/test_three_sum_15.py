import pytest

from three_sum_15 import Solution


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
    ],
)
def test_brute_force_solution(numbers, expected):
    bruteForceSolution = Solution()
    result = bruteForceSolution.threeSum(numbers)
    assert all(inner in expected for inner in result) and len(result) == len(expected)
