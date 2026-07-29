class Solution:
    def trap(self, height: List[int]) -> int:
        # 存左边最高和右边最高的高度
        n = len(height)
        max_left, max_right = [0]*n, [0]*n
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], height[i-1])
        for i in range(n-2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i+1])
        # 接住的雨水量 = min(l, r)-height[i]
        res = 0
        for i in range(n):
            res += max(min(max_left[i], max_right[i])-height[i], 0)
        return res



