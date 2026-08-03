class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # res要做成字典
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] += 1
            res[tuple(count)].append(s) # 这里要记得传转化成tuple的数组，作为哈希键
        return list(res.values()) # 转化成list