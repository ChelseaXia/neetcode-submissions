class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 考虑用滑动窗口
        # 只要这个窗口里面满足了子串，就开始缩短左窗口
        # 如果左窗口缩完之后不满足了，右边窗口再走
        if len(s) < len(t):
            return ""
        need = Counter(t)
        window = defaultdict(int)
        valid = 0 # 标记当前满足子串中的字符数
        ch_need = len(need) # 记录需要满足的字符数
        l = 0 # 标记当前窗口的左端点
        start = 0 # 标记最短窗口的左端点
        min_len = float('inf')
        for r in range(len(s)):
            window[s[r]] += 1
            if need[s[r]] == window[s[r]]:
                valid += 1
            while valid == ch_need: # 覆盖子串了，开始收缩左端点直到不满足
                cur_len = r-l+1
                if cur_len < min_len:
                    start = l # 更新最短窗口的左端点
                    min_len = cur_len # 更新最短长度
                window[s[l]] -= 1 # 左端点开始收缩
                if window[s[l]] < need[s[l]]:
                    valid -= 1
                l += 1
        return s[start: start+min_len] if min_len != float('inf') else ""



