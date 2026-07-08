class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        max_freq = 0
        n = len(s)
        l = 0
        ch_map = [0] * 26
        for r in range(n):
            ch_map[ord(s[r])-ord('A')] += 1
            max_freq = max(ch_map[ord(s[r])-ord('A')], max_freq)
            if max_freq + k < r-l+1:
                ch_map[ord(s[l])-ord('A')] -= 1
                l += 1
            res = max(res, r-l+1)
        return res

