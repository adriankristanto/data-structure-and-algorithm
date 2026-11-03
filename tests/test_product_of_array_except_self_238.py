import pytest

from product_of_array_except_self_238 import Solution


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([1, 2, 0, 4], [0, 0, 8, 0]),
        ([1, 0, 3, 0], [0, 0, 0, 0]),
    ],
)
def test_product_of_array_except_self_238(nums: list[int], expected: list[int]):
    solution = Solution()
    result = solution.productExceptSelf(nums)
    assert result == expected
