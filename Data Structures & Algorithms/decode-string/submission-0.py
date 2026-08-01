class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_str = ""
        cur_num = 0
        for ch in s:
            if ch.isdigit():
                cur_num = cur_num * 10 + int(ch)
            elif ch == '[':
                stack.append((cur_str, cur_num))
                cur_str = "" # 清空
                cur_num = 0 # 清空
            elif ch == ']':
                # 要弹出开始拼接了
                last_str, cur_num = stack.pop()
                cur_str = last_str + cur_num * cur_str
                cur_num = 0 # 这里要注意把cur_num清零
            else:
                cur_str += ch
        return cur_str