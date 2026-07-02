class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            if target-num in hashmap:
                return [hashmap[target-num], i]
            if num not in hashmap:
                hashmap[num] = i
        return []