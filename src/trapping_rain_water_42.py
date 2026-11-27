class Solution:
    def trap(self, heights: list[int]) -> int:
        return 0


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
