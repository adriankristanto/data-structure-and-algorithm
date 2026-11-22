class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = [c for c in s.lower() if c.isalnum()]
        return clean == list(reversed(clean))


if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama"))
