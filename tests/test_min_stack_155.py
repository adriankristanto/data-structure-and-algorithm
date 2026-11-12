import pytest

from min_stack_155 import MinStack


@pytest.fixture
def stack():
    return MinStack()


@pytest.mark.parametrize("value", [5, 10, 20, -1, -5, 0])
def test_push_and_get_top(stack, value):
    stack.push(value)
    assert stack.top() == value


@pytest.mark.parametrize("values", [[1, 2, 3], [-3, -2, -1]])
def test_pop(stack, values):
    for value in values:
        stack.push(value)

    for expected_top in reversed(values):
        assert stack.top() == expected_top
        stack.pop()


@pytest.mark.parametrize(
    "values",
    [
        [1, 2, 3],
        [3, 2, 1],
        [3, 1, 1],
        [-5, -7, -2],
    ],
    ids=["ascending-values", "descending-values", "duplicates", "negative-values"],
)
def test_minimum_tracking(stack, values):
    for value in values:
        stack.push(value)
    for i in range(len(values)):
        assert stack.getMin() == min(values[: len(values) - i])
        stack.pop()
