class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        sortedNums = sorted(nums)

        lengths = []
        length = 0
        for i in range(1, len(sortedNums)):
            if abs(sortedNums[i] - sortedNums[i - 1]) == 1:
                length += 1
            elif abs(sortedNums[i] - sortedNums[i - 1]) == 0:
                continue
            else:
                length += 1  # account for the last element
                lengths.append(length)
                length = 0
        length += 1  # account for the last element
        lengths.append(length)

        return max(lengths)


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))
