class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        # 把matrix[i][j]换到matrix[j][n-i-1]
        # 考虑先对角线调换，然后再翻转矩阵
        for i in range(m):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(m):
            matrix[i].reverse()
