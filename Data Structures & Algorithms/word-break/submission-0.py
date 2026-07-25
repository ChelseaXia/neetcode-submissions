class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 用dp存从开头到当前这一段是否能被拆分
        wdict = set(wordDict)
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wdict:
                    dp[i] = True
        return dp[n]
        

