class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # brute force O(n^2) since we have to iterate through the list n^2 times
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # use O(n) space and time
        # only goes through each number once (store it inside a hash table)
        occurences: dict[int, int] = {}
        for num in nums:
            if num in occurences:
                return True
            occurences[num] = 1
        # worst case: when no duplicates
        return False


if __name__ == "__main__":
    solution: Solution = Solution()
    print(solution.containsDuplicate([1, 2, 3, 1]))
