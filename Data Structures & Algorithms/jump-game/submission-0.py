class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 维护一个max_jump，每走到一个地方看看是不是max_jump能到的地方，不能就到不了了
        max_jump = 0
        for i, num in enumerate(nums):
            if max_jump < i:
                return False
            max_jump = max(max_jump, i+num) # 注意这里比较的是max_jump和num+i
            if i >= len(nums)-1:
                return True
            