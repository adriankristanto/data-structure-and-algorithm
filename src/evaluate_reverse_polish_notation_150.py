from collections.abc import Callable


def divide(x, y):
    quotient = abs(x) // abs(y)
    # if both are positives or negatives, then the result is positive
    # if either one is negative, then the result is negative
    sign = -1 if (x < 0) != (y < 0) else 1
    return sign * quotient


class Solution:
    def evalRPN(self, token: list[str]) -> int:
        stack: list[int] = []
        operators: dict[str, Callable[[int, int], int]] = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": divide,
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
