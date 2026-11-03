class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded = []
        for content in strs:
            length = len(content)
            encoded.append(f"{length}#{content}")
        return "".join(encoded)

    def decode(self, s: str) -> list[str]:
        decoded = []
        pointer = 0
        while pointer < len(s):
            length = 0
            while s[pointer].isdigit():
                # we shouldn't do int(s[pointer]) * 10 since this will result in the last element being multiplied by 10, e.g., if the length should have been 3, it will end up with 30
                length = length * 10 + int(s[pointer])
                pointer += 1
            # skip the separator #, and move to the start of the string
            pointer += 1
            content = s[pointer : pointer + length]
            decoded.append(content)
            pointer += length
        return decoded


if __name__ == "__main__":
    solution = Solution()
    encoded = solution.encode(["hello,world", "hello", "world"])
    print(encoded)
    decoded = solution.decode(encoded)
    print(decoded)
