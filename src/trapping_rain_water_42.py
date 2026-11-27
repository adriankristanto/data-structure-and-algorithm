class Solution:
    def trap(self, heights: list[int]) -> int:
        # exclude the current bar from prefix/suffix
        prefix: list[int] = [0] * len(heights)
        for i in range(1, len(heights) - 1):
            prefix[i] = max(prefix[i - 1], heights[i - 1])
        suffix: list[int] = [0] * len(heights)
        for j in range(len(heights) - 2, 0, -1):
            suffix[j] = max(suffix[j + 1], heights[j + 1])
        total = 0
        for k in range(1, len(heights) - 1):
            # if the current bar is the tallest, the result will be negative, so add max(0, ...)
            area = max(0, min(prefix[k], suffix[k]) - heights[k])
            total += area
        return total


class BruteForceSolution:
    def trap(self, heights: list[int]) -> int:
        total = 0
        # the first and last bar cannot hold any water
        for i in range(1, len(heights) - 1):
            leftTallest = max(heights[:i])
            rightTallest = max(heights[i + 1 :])
            shorterTallest = min(leftTallest, rightTallest)
            # the following can be -ve, e.g., if the current height is the tallest, then the result will be -ve
            water = shorterTallest - heights[i]
            total += max(0, water)
        return total


if __name__ == "__main__":
    solution = BruteForceSolution()
    print(solution.trap([4, 2, 0, 3, 2, 5]))
