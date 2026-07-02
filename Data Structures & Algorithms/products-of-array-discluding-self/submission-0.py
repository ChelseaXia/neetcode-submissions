class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [0] * length
        p_all = 1
        zero_flag = 0
        for i, num in enumerate(nums):
            if num == 0:
                p_all = 0
                zero_flag += 1
            else:
                p_all *= num
        if zero_flag >= 2:
            res = [0] * length
        elif zero_flag == 1:
            p_left = 1
            flag = 0
            for i, num in enumerate(nums):
                if num == 0:
                    flag = i
                    continue
                p_left *= num
            res[flag] = p_left
        else:
            for i, num in enumerate(nums):
                res[i] = int(p_all/num)
        return res
                
            
            
            
            
        