from collections import defaultdict


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        l1, l2 = len(s), len(p)
        target = defaultdict(int)
        for c in p:
            target[c] += 1
        cur_window = defaultdict(int)
        start, end = 0, 0
        while end < l1:
            cur_window[s[end]] += 1
            if end - start + 1 == l2:
                if cur_window == target:
                    res.append(start)
                cur_window[s[start]] -= 1
                if cur_window[s[start]] == 0:
                    del cur_window[s[start]]
                start += 1
            end += 1
        return res
