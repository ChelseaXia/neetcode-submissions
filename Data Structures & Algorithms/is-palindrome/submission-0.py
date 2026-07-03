class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join(ch.lower() for ch in s if ch.isalnum())
        n = len(new_s)
        for i in range(n//2):
            if new_s[i] != new_s[n-1-i]:
                return False
        return True