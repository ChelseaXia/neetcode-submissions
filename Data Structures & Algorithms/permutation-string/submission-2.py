class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        count2 = {}
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        for ch in s1:
            count1[ch] = count1.get(ch, 0) + 1
        for i in range(n1):
            count2[s2[i]] = count2.get(s2[i], 0) + 1
        if count1 == count2:
            return True
        else:
            for i in range(n1, n2):
                count2[s2[i-n1]] -= 1
                if count2[s2[i-n1]] == 0:
                    del count2[s2[i-n1]]
                count2[s2[i]] = count2.get(s2[i], 0) + 1
                if count1 == count2:
                    return True
        return False