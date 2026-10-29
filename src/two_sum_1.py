class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # for i in range(0, len(nums)):
        #   for j in range(i + 1, len(nums)):
        #       if nums[i] + nums[j] == target:
        #           return [i, j]
        # unreachable -- we can assume that there is always one result
        # return []
        
        record: dict[int, int] = {}
        for (i, num) in enumerate(nums):
            result = target - num
            if result in record:
                return [record[result], i]
            # it's safe to overwrite the previous result, e.g., nums is [3,3,4,5] and target is 9 
            # we don't care whether 3 is the first one or the second one
            # also, [3,3,4] and target is 7 is not possible since there are two solutions here
            record[num] = i
        raise ValueError("No two numbers add up to the target.")
