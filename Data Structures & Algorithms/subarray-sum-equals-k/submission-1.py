class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 考虑用前缀和来做
        pre = 0
        count = defaultdict(int)
        res = 0
        count[0] = 1 # 前缀和为0的就是一个也不加
        for num in nums:
            pre += num
            # 注意要先查询后更新，不然会多算当前的位置
            res += count[pre-k]
            count[pre] += 1
        return res