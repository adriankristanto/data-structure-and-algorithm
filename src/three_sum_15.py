class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        sortedNums = sorted(nums)
        # minus 2 since we only want to search to the right of target (index i) -- since the list is now sorted, if we use one target c and find all possible ways that sums up to c, then we no longer need to consider any prior targets -> so, only look to the right of the currently selected target
        i = 0
        while i < len(sortedNums) - 2:
            # multiply by -1 since we are moving the target to the left
            # i.e., smallest + largest + target = 0
            # so, smallest + largets = -target
            currentNumber = sortedNums[i]

            # note the property of a sorted list
            # currentNumber <= currentSmallest <= currentLargest
            # if currentNumber > 0, then currentSmallest and currentLargest are both > 0
            # which means if currentNumber > 0, then currentNumber + currentLargest + currentSmallest > 0, we can never meet the condition currentNumber + currentSmallest + currentLargest = 0, so it's save to terminate early here (pruning)
            # if currentNumber = 0, however, it is possible that currentSmallest and currentLargest be 0, see the example [0, 0, 0] -- not safe to terminate early
            if currentNumber > 0:
                return result

            target = -1 * currentNumber
            smallest = i + 1
            largest = len(sortedNums) - 1
            while smallest < largest:
                currentSmallest = sortedNums[smallest]
                currentLargest = sortedNums[largest]

                total = currentSmallest + currentLargest

                if total == target:
                    # no longer need sorting since the input array is now sorted
                    result.append([currentNumber, currentSmallest, currentLargest])
                    # we can move both because, given the same nums[i], using the same nums[smallest] or nums[largest] will always give back the same number as the other operand, e.g., a + b = c -- given the same c and a, b will always be the same, so skip the same b and a
                    while (
                        smallest < largest and sortedNums[smallest] == currentSmallest
                    ):
                        smallest += 1
                    while smallest < largest and sortedNums[largest] == currentLargest:
                        largest -= 1
                    continue

                if total < target:
                    while (
                        smallest < largest and sortedNums[smallest] == currentSmallest
                    ):
                        smallest += 1
                    continue

                while smallest < largest and sortedNums[largest] == currentLargest:
                    largest -= 1

            while i < len(sortedNums) - 2 and sortedNums[i] == currentNumber:
                i += 1

        return result


class BruteForceSolution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if (
                        nums[i] + nums[j] + nums[k] == 0
                        and sorted([nums[i], nums[j], nums[k]]) not in result
                    ):
                        result.append(sorted([nums[i], nums[j], nums[k]]))
        return result


if __name__ == "__main__":
    solution = Solution()
    result = solution.threeSum([-1, 0, 1, 2, -1, -4])
    print(result)
