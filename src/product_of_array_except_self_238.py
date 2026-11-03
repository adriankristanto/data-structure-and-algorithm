class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left_product = 1
        right_product = 1
        start = 0
        end = len(nums) - 1
        i = 0
        result = [1 for _ in nums]
        while i < len(nums):
            # update the result array first before updating the cumulative product -- otherwise the current element will be included
            result[start] *= left_product
            left_product *= nums[start]
            start += 1
            result[end] *= right_product
            right_product *= nums[end]
            end -= 1
            i += 1
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf([1, 2, 3, 4]))
