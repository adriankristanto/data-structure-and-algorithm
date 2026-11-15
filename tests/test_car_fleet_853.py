import pytest

from car_fleet_853 import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize("target, position, speed, expected", [(10, [3], [3], 1)])
def test_single_car(solution, target, position, speed, expected):
    result = solution.carFleet(target, position, speed)
    assert result == expected


@pytest.mark.parametrize(
    "target, position, speed, expected", [(100, [0, 2, 4], [4, 2, 1], 1)]
)
def test_large_target(solution, target, position, speed, expected):
    result = solution.carFleet(target, position, speed)
    assert result == expected


@pytest.mark.parametrize("target, position, speed, expected", [(10, [6, 8], [3, 2], 2)])
def test_fractional_arrival_times(solution, target, position, speed, expected):
    result = solution.carFleet(target, position, speed)
    assert result == expected
