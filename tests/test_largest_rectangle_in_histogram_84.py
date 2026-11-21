import pytest

from largest_rectangle_in_histogram_84 import Solution, BruteForceSolution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "heights",
    [[7, 1, 7, 2, 2, 4], [1, 3, 7], [2, 1, 5, 6, 2, 3], [2, 4], [4, 5, 3, 6, 2]],
)
def test_largest_rectangle_in_histogram(solution, heights):
    result = solution.largestRectangleArea(heights)
    bruteForceResult = BruteForceSolution().largestRectangleArea(heights)
    assert result == bruteForceResult
