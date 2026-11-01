import pytest

from top_k_frequent_elements_347 import Solution


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        ([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2, [1, 2]),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
    ],
)
def test_top_k_frequent_elements_347(nums, k, expected):
    solution = Solution()
    result = solution.topKFrequent(nums, k)
    assert sorted(result) == sorted(expected)
