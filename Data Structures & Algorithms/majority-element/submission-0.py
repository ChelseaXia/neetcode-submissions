class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 摩尔投票法，一个存当前出现次数最多值，一个存出现次数
        # 如果下一个数字不是cur_num，出现次数减1，直到减到0，cur_num变成0
        # 最终cur_num一定是出现次数最多的数
        cur_num, cur_times = 0, 0 
        for num in nums:
            if num == cur_num:
                cur_times += 1
            else:
                if cur_times == 0:
                    cur_num = num
                    cur_times += 1
                else:
                    cur_times -= 1
                    if cur_times == 0:
                        cur_num = 0
        return cur_num