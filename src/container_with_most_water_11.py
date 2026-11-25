class Solution:
    def maxArea(self, heights: list[int]) -> int:
        left = 0
        right = len(heights) - 1
        largest = 0
        while left < right:
            leftHeight = heights[left]
            rightHeight = heights[right]
            limitingHeight = min(leftHeight, rightHeight)
            width = right - left
            largest = max(largest, limitingHeight * width)
            # the insight:
            # 0. going inwards means shorter width, so if the height is also shorter == smaller area
            # 1. given the current height, we cannot improve the area by moving inward if the next height is shorter or equal to the current height, so we need to find the next height that's taller than the current height
            # this applies to both left and right
            # 2. if both heights are equal, we can move both pointer inwards until we find a taller height on each side
            # otherwise, either one of the heights will become the limiting height, so regardless of the height chosen by the other pointer, the area will not improve.
            while left < right and heights[left] <= limitingHeight:
                left += 1
            while left < right and heights[right] <= limitingHeight:
                right -= 1
        return largest


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
    result = solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(result)
