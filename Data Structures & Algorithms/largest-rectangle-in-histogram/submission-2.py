class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 考虑用单调递增栈，栈内存高度下标
        # while循环，如果遇到了比栈顶更小的高度，开始结算
        # 弹出栈顶，高度为栈顶，宽度为当前走到的高度的下标i - 弹出栈顶后的新栈顶 - 1（可以手推一下），如果弹出后栈为空，长度就是i
        # 一个小trick：为了避免后续额外处理栈内剩余元素，可以额外对高度序列补充一个为0的高度
        stack = []
        heights.append(0)
        max_area = 0
        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                h_idx = stack.pop()
                w = i if not stack else i-stack[-1]-1
                max_area = max(max_area, heights[h_idx] * w)
            stack.append(i)
        return max_area
