class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix_product: list[int] = [num for num in nums]
        for i in range(len(nums)):
            if i != 0:
                prefix_product[i] = prefix_product[i - 1] * nums[i]

        suffix_product = [num for num in nums]
        for j in range(len(nums) - 1, -1, -1):
            if j != len(nums) - 1:
                suffix_product[j] = suffix_product[j + 1] * nums[j]

        result = [num for num in nums]
        for k in range(len(nums)):
            if k == 0:
                result[k] = suffix_product[k + 1]
                continue
            if k == len(nums) - 1:
                result[k] = prefix_product[k - 1]
                continue
            result[k] = prefix_product[k - 1] * suffix_product[k + 1]
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf([1, 2, 3, 4]))
