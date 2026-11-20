class Solution:
    # this is solved using prefix/suffix array combined with monotonic stack
    # the stack must be monotonically increasing (strictly) -- since
    # rectangle can still be formed if the previous bar has the same height as the current bar, so we pop even if the heights are equal
    # the main idea is that, if the previous bar is taller, then we can use the previous' bar boundary (which is why I stored the previous bar's height and boundary in the stack -- the height is what causes the stack to be monotonically increasing, while the boundary is the prefix/suffix technique)
    # if the previous bar is shorter, then we use the current bar as the current bar's own boundary
    def largestRectangleArea(self, heights: list[int]) -> int:
        leftBounds = [i for i in range(len(heights))]
        leftStack = []
        for j in range(len(heights)):
            while len(leftStack) > 0 and leftStack[-1][1] >= heights[j]:
                idx, _ = leftStack.pop()
                leftBounds[j] = idx
            leftStack.append((leftBounds[j], heights[j]))

        rightBounds = [i for i in range(len(heights))]
        rightStack = []
        for k in range(len(heights) - 1, -1, -1):
            while len(rightStack) > 0 and rightStack[-1][1] >= heights[k]:
                idx, _ = rightStack.pop()
                rightBounds[k] = idx
            rightStack.append((rightBounds[k], heights[k]))

        largest = 0
        for l in range(len(heights)):
            height = heights[l]
            width = rightBounds[l] - leftBounds[l] + 1
            area = height * width
            largest = max(largest, area)
        return largest


class BruteForceSolution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        largest = 0
        for i in range(len(heights)):

            left = 0
            j = i - 1
            while j >= 0 and heights[j] >= heights[i]:
                left += 1
                j -= 1

            right = 0
            k = i + 1
            while k < len(heights) and heights[k] >= heights[i]:
                right += 1
                k += 1

            largest = max(largest, heights[i] * (left + 1 + right))

        return largest


if __name__ == "__main__":
    solution = Solution()
    input = [7, 1, 7, 2, 2, 4]
    result = solution.largestRectangleArea(input)
    correct = BruteForceSolution().largestRectangleArea(input)
    print(result)
    print(correct)
