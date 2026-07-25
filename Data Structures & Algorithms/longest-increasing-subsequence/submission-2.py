import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 维护一个tails数组，下标为k的位置存长度为k+1的子序列的末尾最小值
        tails = []
        for num in nums:
            idx = bisect.bisect_left(tails, num)
            if idx == len(tails):
                tails.append(num)
            else:
                tails[idx] = num
        return len(tails)