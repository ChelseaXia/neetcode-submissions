from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = deque()
        res = []
        for i in range(n):
            # 把小的挤出去
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            # 把不在窗口内的挤出去
            while q[0] <= i-k:
                q.popleft()
            # 达到窗口大小，可以开始产出答案
            if i >= k-1:
                res.append(nums[q[0]])
        return res
