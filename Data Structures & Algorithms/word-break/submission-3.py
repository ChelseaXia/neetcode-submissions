from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 考虑dfs的做法，但是要用cache自动记忆化DFS返回值
        wdict = set(wordDict)
        n = len(s)
        @cache
        def dfs(start):
            if start == n: return True
            for i in range(start, n):
                if s[start:i+1] in wdict:
                    if dfs(i+1):
                        return True
            return False
        return dfs(0)
        

