class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 记住start和max_len就好
        n = len(s)
        def length(l, r):
            while 0<=l<n and 0<=r<n and s[l] == s[r]:
                l -= 1
                r += 1
            return r-l-1
        start, max_len = 0, 0
        for i, ch in enumerate(s):
            length1 = length(i, i)
            length2 = length(i, i+1)
            if max(length1, length2) >= max_len:
                if length1 >= length2:
                    max_len = length1
                    start = i - length1//2
                else:
                    max_len = length2
                    start = i - (length2-1)//2
        return s[start: start+max_len]
                
