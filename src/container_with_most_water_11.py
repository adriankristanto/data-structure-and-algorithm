class Solution:
    def maxArea(self, heights: list[int]) -> int:
        return 0


class BruteForceSolution:
    def maxArea(self, heights: list[int]) -> int:
        largest = 0
        for i in range(len(heights) - 1):
            for j in range(i + 1, len(heights)):
                h = min(heights[i], heights[j])
                w = j - i
                largest = max(largest, h * w)
        return largest


if __name__ == "__main__":
    solution = Solution()
    solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
