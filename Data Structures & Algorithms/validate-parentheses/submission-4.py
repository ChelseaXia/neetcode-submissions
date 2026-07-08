class Solution:
    def isValid(self, s: str) -> bool:
        cmap = {
            '{': '}',
            '(': ')',
            '[': ']'
        }
        stack = []
        for ch in s:
            if ch in cmap:
                stack.append(ch)
            elif stack and ch == cmap[stack[-1]]:
                stack.pop()
            else:
                return False
        return False if stack else True