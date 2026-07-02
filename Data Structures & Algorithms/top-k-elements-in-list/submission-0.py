class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        freq_list = []
        for num, freq in count.items():
            freq_list.append((freq, num))
        freq_list = sorted(freq_list, key = lambda x:x[0], reverse=True)
        res = []
        for i in range(k):
            res.append(freq_list[i][1])
        return res
        

