class Solution:
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