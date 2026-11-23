class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        smallest = 0
        largest = len(numbers) - 1
        while smallest < largest:
            total = numbers[smallest] + numbers[largest]
            if total == target:
                return [smallest + 1, largest + 1]
            # if target - largest is larger than smaller, we need to move smaller up
            if total < target:
                smallest += 1
                continue
            
            # if target - largest is smaller than smallest, move largest down
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
