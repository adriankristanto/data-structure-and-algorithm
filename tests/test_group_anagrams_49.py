import pytest

from group_anagrams_49 import Solution
from collections.abc import Callable


def flatmap[T, U](f: Callable[[T], list[U]], lst: list[T]) -> list[U]:
    nested = list(map(f, lst))
    return [elem for inner in nested for elem in inner]


@pytest.mark.parametrize(
    "strs, expected",
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ],
)
def test_group_anagrams_49(strs, expected):
    solution = Solution()
    result = solution.groupAnagrams(strs)
    assert sorted(flatmap(sorted, result)) == sorted(flatmap(sorted, expected))
