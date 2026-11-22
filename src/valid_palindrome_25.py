from collections.abc import Callable


def zipWith[t, u, v](f: Callable[[t, u], v], xs: list[t], ys: list[u]) -> list[v]:
    return [f(x, y) for x, y in zip(xs, ys)]


class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = [c for c in s.lower() if c.isalnum()]
        return all(zipWith(lambda x, y: x == y, clean, list(reversed(clean))))


if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama"))
