class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = []
        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplets.append([nums[i], nums[j], nums[k]])
        result = []
        for triplet in triplets:
            if sorted(triplet) not in result:
                result.append(sorted(triplet))
        return result


if __name__ == "__main__":
    solution = Solution()
    result = solution.threeSum([-1, 0, 1, 2, -1, -4])
    print(result)
