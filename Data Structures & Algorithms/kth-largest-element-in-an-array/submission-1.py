class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 维护一个小顶堆
        # 当堆的大小超过k时，开始弹出元素
        # 最后留下来的堆顶就是第k大的数
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]