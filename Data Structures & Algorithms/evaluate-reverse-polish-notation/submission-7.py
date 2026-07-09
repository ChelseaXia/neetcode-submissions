class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for ch in tokens:
            if ch not in ("+", "-", "*", "/"):
                s.append(int(ch))
            else:
                b = s.pop()
                a = s.pop()
                if ch == "+":
                    s.append(a+b)
                elif ch == "-":
                    s.append(a-b)
                elif ch == "*":
                    s.append(a*b)
                elif ch == "/":
                    s.append(int(a/b))
        return int(s.pop())