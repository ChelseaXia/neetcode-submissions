class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(path, l ,r):# 维护一个左括号数和一个右括号数
            if len(path) == 2*n:
                res.append("".join(path))
                return
            if l < n: # 左括号数必须小于n
                path.append('(')
                dfs(path, l+1, r)
                path.pop()
            if r < l: # 右括号数必须小于左括号数
                path.append(')')
                dfs(path, l, r+1)
                path.pop()
        dfs([], 0, 0)
        return res
            