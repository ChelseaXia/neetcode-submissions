class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []
        for c in s:
            if c in mapping:
                stack.append(c)
            else:
                if stack:
                    l = stack[-1]
                    if mapping[l] == c:
                        stack.pop()
                    else: return False
                else:
                    return False
        return False if stack else True