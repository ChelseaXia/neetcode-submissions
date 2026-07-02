class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        freq_list = list(count.items())
        freq_list = sorted(freq_list, key = lambda x:x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(freq_list[i][0])
        return res
        

