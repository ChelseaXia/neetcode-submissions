class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if not s:
            return []
        start, end = 0, 0
        max_len = 0
        def extension(l, r):
            while 0 <= l < n and 0 <= r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return (r-1)-(l+1)+1 # 返回回文子串的长度
        for i in range(n):
            cur_len1 = extension(i, i)
            cur_len2 = extension(i, i+1)
            cur_len = max(cur_len1, cur_len2)
            if cur_len > max_len:
                start = i - (cur_len-1)//2
                end = i + cur_len//2
                max_len = cur_len
        return s[start:end+1]
