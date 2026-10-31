class Solution:
    # assumption: can only include lowercase English character
    def charToIndex(self, char: str) -> int:
        return ord(char) - ord("a")

    # arbitrary size tuple as type hint can be defined as tuple[int, ...]
    # returns a tuple since in python it is immutable and hashable
    # O(m) for encoding instead of O(m log m) when sorting
    def encode_frequency(self, string: str) -> tuple[int, ...]:
        frequency_list: list[int] = [0] * 26
        # given an empty string, this loop will immediately stop
        # then return the frequency_list with all 0's
        for char in string:
            frequency_list[self.charToIndex(char)] += 1
        return tuple(frequency_list)

    # so, time complexity is O(n x m -> for each string, encode the string of maximum length m)
    # space complexity is O(n), since for each string, we store a fixed list of size 26
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # seen_anagram: dict[str, list[str]] = {}
        # for string in strs:
        #     sorted_string = "".join(sorted(string))
        #     if sorted_string in seen_anagram:
        #         seen_anagram[sorted_string].append(string)
        #     else:
        #         seen_anagram[sorted_string] = [string]
        # return [group for group in seen_anagram.values()]

        seen_anagram: dict[tuple[int, ...], list[str]] = {}
        for string in strs:
            encoded = self.encode_frequency(string)
            if encoded in seen_anagram:
                seen_anagram[encoded].append(string)
            else:
                seen_anagram[encoded] = [string]
        return [group for group in seen_anagram.values()]


if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams([""]))
