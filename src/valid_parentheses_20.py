class Solution:
    def isValid(self, s: str) -> bool:
        pairs: dict[str, str] = {")": "(", "}": "{", "]": "["}
        stack: list[str] = []
        for c in s:
            # if the character is one of the opening brackets
            # we can make this assumption since one constraint is the brackets can either be () [] or {}
            if c not in pairs:
                stack.append(c)
                continue
            # if the character is one of the closing brackets
            # return invalid if
            # the stack is empty (no corresponding opening bracket)
            # or
            # the last opening bracket doesn't correspond to the current closing bracket
            if len(stack) == 0 or stack.pop() != pairs[c]:
                return False

        return len(stack) == 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("({[]})"))
