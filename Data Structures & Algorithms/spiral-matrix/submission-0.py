class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 左、右、下、上一直循环
        left, right = 0, len(matrix[0])-1
        bottom, top = len(matrix)-1, 0
        res = []
        while left <= right and top <= bottom:
            # 遍历上
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1
            # 遍历右
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1
            # 遍历下
            if top <= bottom: # 这里注意要判空，因为走了一轮不确定是否还满足
                for i in range(right, left-1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
            # 遍历左
            if left <= right: # 这里也要加一个判断
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res
