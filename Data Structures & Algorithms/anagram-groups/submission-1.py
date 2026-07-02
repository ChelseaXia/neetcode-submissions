class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        n = len(strs)
        flags = [0] * n
        for i, str1 in enumerate(strs):
            if flags[i] == 1:
                continue
            res = [str1]
            flags[i] = 1
            for j in range(i+1, n):
                if flags[j] == 1:
                    continue
                if self.isAnagram(str1, strs[j]):
                    res.append(strs[j])
                    flags[j] = 1
            ans.append(res)
        return ans
    
    def isAnagram(self, str1, str2):
        if len(str1) != len(str2):
            return False
        count1, count2 = {}, {}
        for i in range(len(str1)):
            count1[str1[i]] = 1 + count1.get(str1[i], 0)
            count2[str2[i]] = 1 + count2.get(str2[i], 0)
        if count1 == count2:
            return True
                