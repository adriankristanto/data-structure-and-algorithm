class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        if (len(temperatures)) == 0:
            return []

        result = [0 for _ in range(len(temperatures))]
        stack: list[int] = []
        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                previousIndex = stack.pop()
                result[previousIndex] = i - previousIndex
            stack.append(i)

        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
