class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = [c for c in s.lower() if c.isalnum()]

        left = 0
        right = len(clean) - 1
        result = True
        while left < right:
            result = result and clean[left] == clean[right]
            left += 1
            right -= 1
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama"))
