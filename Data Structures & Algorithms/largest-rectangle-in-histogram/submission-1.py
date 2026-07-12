class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        heights.append(0)
        stack = []
        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                h_idx = stack.pop()
                # 这里要注意右边界不是h_idx，而是当前遍历到的i-1
                w = i if not stack else (i-stack[-1]-1)
                max_area = max(max_area, w*heights[h_idx])
            stack.append(i)
        return max_area



