class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left_cummulative_product = 1
        right_cummulative_product = 1
        start = 0
        end = len(nums) - 1
        i = 0
        result = [1 for _ in nums]
        while i < len(nums):
            result[start] *= left_cummulative_product
            left_cummulative_product *= nums[start]
            start += 1
            result[end] *= right_cummulative_product
            right_cummulative_product *= nums[end]
            end -= 1
            i += 1
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf([1, 2, 3, 4]))
