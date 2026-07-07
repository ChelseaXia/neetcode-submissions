class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest = 0
        char_map = defaultdict(int)
        l = 0
        for i in range(n):
            if s[i] not in char_map or char_map[s[i]] < l:
                longest = max(longest, i-l+1)
            else:
                l = char_map[s[i]] + 1
            char_map[s[i]] = i
        return longest
            
                