class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left_product = 1
        right_product = 1
        # avoid mutable references here, e.g., [[]] * len(nums) will create a list of references to the same inner list, which is not what we want -- I know that a list of integers is fine since integers are immutable, but I want to be consistent and avoid mutable references in general
        result = [1 for _ in nums]
        for i in range(len(nums)):
            # update the result array first before updating the cumulative product -- otherwise the current element will be included
            result[i] *= left_product
            left_product *= nums[i]
            result[len(nums) - i - 1] *= right_product
            right_product *= nums[len(nums) - i - 1]
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf([1, 2, 3, 4]))
