class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        # 用滑动窗口做
        start, end = 0, 0
        max_len = 0
        while start <= end and end < len(s):
            if s[end] in char_map and char_map[s[end]] >= start:
                start = char_map[s[end]] + 1
            max_len = max(max_len, end-start+1)
            char_map[s[end]] = end # 无论如何都需要更新字典位置
            end += 1
        return max_len
