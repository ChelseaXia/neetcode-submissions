class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        # 用双端队列
        # 存下标，维护一个下标对应的数组里的数是递减的，只要你不是最大值，你就没有存在的价值，可以直接弹出去
        q = deque()
        for i, num in enumerate(nums):
            while q and num > nums[q[-1]]: 
                q.pop() # 从右边弹出去
            q.append(i)
            while q[0] <= i-k:
                q.popleft() # 超过窗口大小，队首从左边弹出去
            if i >= k-1:
                res.append(nums[q[0]])
        return res
