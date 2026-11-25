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


@pytest.mark.parametrize(
    "heights",
    [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7]),
        ([1, 7, 2, 5, 4, 7, 3, 6]),
        ([1, 1]),
        ([]),
        ([1, 2, 3, 4, 5, 6, 7]),
        ([7, 6, 5, 4, 3, 2, 1]),
        ([1, 2, 3, 2, 1]),
        ([1, 4, 5, 3, 2]),
        ([5, 4, 3, 4, 5]),
        ([5, 2, 1, 3, 4]),
        ([2, 2, 2, 2, 2]),
        ([0, 0, 0, 0]),
        ([0, 1, 2, 3, 4, 5, 0]),
        ([100, 1, 1, 100]),
        ([1, 100, 100, 1]),
        ([100, 1, 100, 1]),
    ],
    ids=[
        "general-1",
        "general-2",
        "minimum-valid-input-size-1",
        "empty-1",
        "increasing-1",
        "decreasing-1",
        "symmetric-peak-1",
        "asymmetric-peak-1",
        "symmetric-valley-1",
        "asymmetric-valley-1",
        "non-zero-plateau-1",
        "zero-plateau-1",
        "zero-outer-1",
        "include-both-outer-1",
        "exclude-both-outer-1",
        "include-one-outer-1",
    ],
)
def test_optimised_solution(heights):
    bruteForceSolution = BruteForceSolution()
    solution = Solution()
    correct = bruteForceSolution.maxArea(heights)
    result = solution.maxArea(heights)
    assert correct == result
