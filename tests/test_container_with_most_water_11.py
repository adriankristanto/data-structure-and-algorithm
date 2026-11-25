import pytest

from container_with_most_water_11 import Solution, BruteForceSolution


@pytest.mark.parametrize(
    "heights, expected",
    [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([1, 2, 3, 4, 5, 6, 7], 12),
        ([7, 6, 5, 4, 3, 2, 1], 12),
        ([1, 7, 2, 5, 4, 7, 3, 6], 36),
        ([2, 2, 2], 4),
    ],
)
def test_brute_force_solution(heights, expected):
    bruteForceSolution = BruteForceSolution()
    result = bruteForceSolution.maxArea(heights)
    assert result == expected
