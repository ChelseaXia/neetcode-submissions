class Solution:
    def jump(self, nums: List[int]) -> int:
        # 维护一个当前跳到的安全区cur_end
        # 维护一个当前能跳到最远的地方next_max_reach
        # 如果当前跳到的位置为安全区最远的地方，就要step+1更新了并且跳到nex_max_reach了
        cur_end = 0
        next_max_reach = 0
        steps = 0
        for i, num in enumerate(nums):
            if cur_end >= len(nums)-1:
                return steps
            next_max_reach = max(next_max_reach, i+num)
            if i == cur_end:
                cur_end = next_max_reach
                steps += 1