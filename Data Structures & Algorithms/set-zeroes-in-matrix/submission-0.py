class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        # 用第一行和第一列打标签，所以要先提前标记这里有没有0
        isFirstRowZero = any(matrix[0][j] == 0 for j in range(cols))
        isFirstColZero = any(matrix[i][0] == 0 for i in range(rows))
        # 开始打标记
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # 根据标记置零
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j] = 0
        # 处理第一行第一列
        if isFirstRowZero:
            for j in range(cols):
                matrix[0][j] = 0
        if isFirstColZero:
            for i in range(rows):
                matrix[i][0] = 0 

        