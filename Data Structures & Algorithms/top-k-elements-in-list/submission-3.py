class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        heap = []
        for key, value in count.items(): # 这里的语法要注意是count.items()
        # 还有一种写法是for num in count.keys(): heapq.heappush(heap, (count[num], num))
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            value, key = heapq.heappop(heap)
            res.append(key)
        return res


