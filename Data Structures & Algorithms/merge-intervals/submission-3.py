class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 先排序，这样每一个区间的起点都会是递增的
        # 对每一对[a, b], [c, d]，a <= c，只需要比较b和c的大小
        # 如果b>=c，那么这两个区间可以被合并为[a, d]（如果d>=b的话）
        intervals.sort(key = lambda x: x[0])
        res = []
        n = len(intervals)
        a, b = intervals[0][0],intervals[0][1]
        if n == 1:
            res.append([a, b])
            return res
        # 当前正在被比较的区间端点
        for i in range(1, n):
            c, d = intervals[i][0], intervals[i][1]
            if b>=c:
                b = d if d>=b else b
            else:
                res.append([a, b])
                a, b = c, d
        res.append([a, b])
        return res




        
