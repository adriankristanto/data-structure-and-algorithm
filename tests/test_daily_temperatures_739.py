import pytest

from daily_temperatures_739 import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "temperatures, expected",
    [([30, 40, 50, 60], [1, 1, 1, 0]), ([30, 60, 90], [1, 1, 0])],
)
def test_increasing_temperature(solution, temperatures, expected):
    result = solution.dailyTemperatures(temperatures)
    assert result == expected


@pytest.mark.parametrize(
    "temperatures, expected",
    [([60, 50, 40, 30], [0, 0, 0, 0]), ([90, 60, 30], [0, 0, 0])],
)
def test_decreasing_temperature(solution, temperatures, expected):
    result = solution.dailyTemperatures(temperatures)
    assert result == expected


@pytest.mark.parametrize(
    "temperatures, expected",
    [([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0])],
)
def test_general_cases(solution, temperatures, expected):
    result = solution.dailyTemperatures(temperatures)
    assert result == expected
