class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = False
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                return True
        return ans