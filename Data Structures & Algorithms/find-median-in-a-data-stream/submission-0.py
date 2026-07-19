class MedianFinder:

    def __init__(self):
        # 大顶堆存前半段比较小的数
        self.max_heap = []
        # 小顶堆存后半段比较大的数
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # 注意这里的heap都是小顶堆，所以如果要做大顶堆的话，需要把数转换成负数
        heapq.heappush(self.max_heap, -num) # 先过一遍大顶堆
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        if len(self.min_heap)>len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        

    def findMedian(self) -> float:
        if len(self.min_heap) != len(self.max_heap):
            return -self.max_heap[0] # 这里注意不要弹出，只是取第一个数
        else: return (self.min_heap[0]-self.max_heap[0])/2
        