class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # a monotonically non-decreasing stack
        # we store the valid left bound for a given histogram
        # i.e., how far left its rectangle can go
        stack: list[tuple[int, int]] = []
        largest = 0

        for i, height in enumerate(heights):
            left = i
            while len(stack) > 0 and stack[-1][1] > height:
                leftBound, h = stack.pop()
                width = i - leftBound
                area = h * width
                largest = max(largest, area)
                left = leftBound
            stack.append((left, height))

        # if the stack is not empty, we still have bars that haven't been handled yet
        # we need to calculate its rectangle
        for j in range(len(stack)):
            leftBound, height = stack[j]
            width = len(heights) - leftBound
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
    arr = [7, 1, 7, 2, 2, 4]
    result = solution.largestRectangleArea(arr)
    correct = BruteForceSolution().largestRectangleArea(arr)
    print("result:", result)
    print("correct:", correct)
