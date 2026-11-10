class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        sortedNums = sorted(nums)

        longest = 0
        left = 0
        right = 1
        while right < len(sortedNums):
            length = 0
            while (
                right < len(sortedNums)
                and abs(sortedNums[left] - sortedNums[right]) <= 1
            ):
                if abs(sortedNums[left] - sortedNums[right]) == 1:
                    length += 1
                left += 1
                right += 1
            length += 1  # to account for the last element
            if longest < length:
                longest = length
            # check for the next sequence (if any)
            left = right
            right += 1
        return longest


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))
