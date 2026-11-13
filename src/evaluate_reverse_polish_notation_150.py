from collections.abc import Callable
import math


class Solution:
    def evalRPN(self, token: list[str]) -> int:
        stack: list[int] = []
        operators: dict[str, Callable[[int, int], int]] = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: math.ceil(x / y) if x / y < 0 else math.floor(x / y),
        }
        for tok in token:
            if tok in operators:
                second = stack.pop()
                first = stack.pop()
                operator = operators[tok]
                result = operator(first, second)
                stack.append(result)
                continue
            stack.append(int(tok))

        return stack.pop()


if __name__ == "__main__":
    solution = Solution()
    print(solution.evalRPN(["2", "1", "+", "3", "*"]))
