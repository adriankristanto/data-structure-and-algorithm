class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = []
        for i in range(len(temperatures) - 1):
            waitTime = 0
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    waitTime = j - i
                    break
            result.append(waitTime)
        result.append(0)  # it it not possible for the last one to wait for a warmer day
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
