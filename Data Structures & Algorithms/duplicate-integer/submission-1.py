class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_map = {}
        for num in nums:
            if num not in num_map:
                num_map[num] = True
            else:
                return True
        return False