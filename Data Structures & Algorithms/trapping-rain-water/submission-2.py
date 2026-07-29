class Solution:
    def trap(self, height: List[int]) -> int:
        # 存左边最高和右边最高的高度
        l_max, r_max = 0, 0
        l, r = 0, len(height)-1
        res = 0
        while l < r:
            if height[l] < height[r]: # 左边是短板，优先处理左边
                if height[l] >= l_max:
                    # 储不了水，更新l_max
                    l_max = height[l]
                else:
                    res += l_max-height[l]
                l += 1
            else: # 反过来也一样
                if height[r] >= r_max:
                    r_max = height[r]
                else:
                    res += r_max-height[r]
                r -= 1
        return res



