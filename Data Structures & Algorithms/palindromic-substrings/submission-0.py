class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        def expand(l, r):
            res = 0
            while 0<=r<n and 0<=l<n and s[l]==s[r]: # 循环条件要注意
                res += 1
                l -= 1
                r += 1
            return res
        count = 0
        for i in range(n):
            count += expand(i, i)
            count += expand(i, i+1)
        return count