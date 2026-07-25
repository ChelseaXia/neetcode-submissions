class Solution:
    def numDecodings(self, s: str) -> int:
        # 算总共有多少种解码方式
        # 每一种字符的解码方式有2种，单独解或者与前面的一起求解，那么
        # dp[i] = dp[i-1]+dp[i-2]
        if not s or s[0]=='0': return 0
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            one = s[i-1]
            if one != '0':
                dp[i] += dp[i-1]
            two = s[i-2:i]
            if 10 <= int(two) <= 26:
                dp[i] += dp[i-2]
        return dp[n]

