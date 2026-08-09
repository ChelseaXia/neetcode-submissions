class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 考虑单调递减栈
        n = len(temperatures)
        stack = [] # 存天数下标
        res = [0] * n
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                res[j] = i-j
            stack.append(i)
        return res