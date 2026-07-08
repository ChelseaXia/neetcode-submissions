class Solution:
    def minWindow(self, s: str, t: str) -> str:
        len1, len2 = len(t), len(s)
        if len1 > len2:
            return ""
        need = Counter(t)
        window = defaultdict(int)
        valid = 0
        ch_need = len(need)
        l = 0
        start = 0 # 标记子串开端
        min_len = float("inf") # 记录最短子串长度 

        for r in range(len2):
            window[s[r]] += 1
            if window[s[r]] == need[s[r]]:
                valid += 1
            while valid == ch_need:
                cur_len = r-l+1
                if cur_len < min_len:
                    min_len = cur_len
                    start = l
                if window[s[l]] == need[s[l]]:
                    valid -= 1
                window[s[l]] -= 1
                l += 1

        return s[start:start+min_len] if min_len != float("inf") else ""

        