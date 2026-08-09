class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_p = prices[0]
        for i, p in enumerate(prices):
            max_profit = max(max_profit, max(0, p-min_p))
            min_p = min(min_p, p)
        return max_profit