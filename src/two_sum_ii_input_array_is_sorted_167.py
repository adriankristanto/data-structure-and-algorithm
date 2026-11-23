class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        smallest = 0
        largest = len(numbers) - 1
        while smallest < largest:
            while smallest < largest and target - numbers[largest] < numbers[smallest]:
                largest -= 1
            while smallest < largest and target - numbers[largest] > numbers[smallest]:
                smallest += 1
            if numbers[smallest] + numbers[largest] == target:
                # + 1 since the answer must be an index (starting from 1, not 0)
                return [smallest + 1, largest + 1]
            # we don't increase the pointer to the smallest number as we might miss something
            largest -= 1
        raise ValueError("No two numbers add up to the target.")


class BruteForceSolution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        raise ValueError("No two numbers add up to the target.")


if __name__ == "__main__":
    solution = Solution()
    result = solution.twoSum([2, 7, 11, 15], 9)
    print(result)
