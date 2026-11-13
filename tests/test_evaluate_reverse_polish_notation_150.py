import pytest

from evaluate_reverse_polish_notation_150 import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "token, expected",
    [
        (["1", "2", "+"], 3),
        (["2", "3", "*"], 6),
        (["8", "3", "/"], 2),
        (["8", "7", "-"], 1),
        (["-8", "3", "/"], -2),
        (["-8", "-3", "/"], 2),
        (["8", "-3", "/"], -2),
    ],
)
def test_simple_expressions(solution, token, expected):
    result = solution.evalRPN(token)
    assert result == expected


@pytest.mark.parametrize(
    "token, expected",
    [
        (["5", "1", "2", "+", "*"], 15),
        (["5", "-1", "2", "*", "*"], -10),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    ],
)
def test_multiple_operations(solution, token, expected):
    result = solution.evalRPN(token)
    assert result == expected
