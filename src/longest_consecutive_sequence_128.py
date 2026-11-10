class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        # to remove duplicates and fast lookup
        unique = set(nums)
        longest = 0
        for num in unique:
            length = 1  # include the start of the current sequence

            # if num - 1 exists, then ignore it since num is not the start of a sequence
            if num - 1 in unique:
                continue

            # follow the sequence
            nextNum = num + 1
            # lookup a set costs O(1) -- similar to a hashmap
            while nextNum in unique:
                length += 1
                nextNum += 1

            # check the length
            longest = max(longest, length)

        return longest


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))
