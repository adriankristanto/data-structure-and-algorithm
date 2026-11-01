import math


class Solution:
    def flatten[T](self, nested_lst: list[list[T]]):
        return [x for nested in nested_lst for x in nested]

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # seen_frequency: dict[int, int] = {}
        # for num in nums:
        #     seen_frequency[num] = (
        #         1 if num not in seen_frequency else seen_frequency[num] + 1
        #     )
        # return list(
        #     map(
        #         lambda x: x[0],
        #         sorted(seen_frequency.items(), key=lambda x: x[1], reverse=True)[:k],
        #     )
        # )

        seen_frequency: dict[int, int] = {}
        for num in nums:
            seen_frequency[num] = seen_frequency.get(num, 0) + 1
        n = len(nums)
        frequency: list[list[int]] = [[] for _ in range(n)]
        for value, freq in seen_frequency.items():
            # we could technically do frequency[freq], but it will create the list in ascending order
            # so, use n - freq, e.g., a value appearing n times will be put at index 0, while an item appearing 0 or 1 time will be placed at the last position
            frequency[n - freq].append(value)
        return self.flatten(frequency)[:k]


if __name__ == "__main__":
    print(Solution().topKFrequent([1], 1))
