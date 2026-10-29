from collections import Counter


class Solution:

    # initial attempt
    # def cleanup(self, string: str) -> str:
    #     return "".join(string.lower().split())

    # def countLetterOccurencesIn(self, string: str) -> dict[str, int]:
    #     occurence: dict[str, int] = {}
    #     for character in self.cleanup(string):
    #         if character in occurence:
    #             occurence[character] += 1
    #         else:
    #             occurence[character] = 0
    #     return occurence

    # def isAnagram(self, s: str, t: str) -> bool:
    #     return self.countLetterOccurencesIn(s) == self.countLetterOccurencesIn(t)

    # Using Counter
    # def cleanup(self, string: str) -> str:
    #     return "".join(string.lower().split())

    # def isAnagram(self, s: str, t: str) -> bool:
    #     return Counter(self.cleanup(s)) == Counter(self.cleanup(t))

    # using frequency array
    def cleanup(self, string: str) -> str:
        return "".join(string.lower().split())

    def isAnagram(self, s: str, t: str) -> bool:
        frequency: list[int] = [0] * 26
        for character in self.cleanup(s):
            # ord('a') only since I assume that we can only have lowercase characters, i.e., "Listen" is the anagram of "Silent"
            # otherwise, ord(character) - ord('a') for lowercase letters (0-25)
            # and ord(character) - ord('A') + 26 for uppercase letters (26-51)
            frequency[ord(character) - ord("a")] += 1
        for character in self.cleanup(t):
            frequency[ord(character) - ord("a")] -= 1
        return all(map(lambda x: x == 0, frequency))


if __name__ == "__main__":
    solution = Solution()
    print(solution.isAnagram("Listen", "Silent"))
