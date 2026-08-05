class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r: # 注意要保障l<r，如果相等的话说明一定是奇数回文串
            while l < r and not s[r].isalnum(): # 这里学会了判断是否是字母数字用char.isalnum()，是否是字母char.isalpha()，是否是数字char.isdigit()
                r -= 1
            while l < r and not s[l].isalnum():
                l += 1
            if s[l].lower() != s[r].lower(): # 注意要小写比较
                return False
            l += 1
            r -= 1
        return True