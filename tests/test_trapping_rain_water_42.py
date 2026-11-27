import pytest

from trapping_rain_water_42 import Solution, BruteForceSolution


@pytest.mark.parametrize(
    "heights, expected",
    [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([0, 2, 0, 3, 1, 0, 1, 3, 2, 1], 9),
        ([5, 0, 4, 0, 3], 7),
    ],
)
def test_brute_force_solution(heights, expected):
    bruteForceSolution = BruteForceSolution()
    result = bruteForceSolution.trap(heights)
    assert result == expected


@pytest.mark.parametrize(
    "heights",
    [
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
        [4, 2, 0, 3, 2, 5],
        [0, 2, 0, 3, 1, 0, 1, 3, 2, 1],
        [5, 0, 4, 0, 3],
    ],
)
def test_optimised_solution(heights):
    bruteForceSolution = BruteForceSolution()
    solution = Solution()
    result = solution.trap(heights)
    correct = bruteForceSolution.trap(heights)
    assert result == correct
