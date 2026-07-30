class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            # 每一行的数量是i+1个
            layer = []
            for j in range(i+1):
                if i <=1 or j == 0 or j == i:
                    layer.append(1)
                else:
                    layer.append(res[-1][j-1]+res[-1][j])
            res.append(layer.copy())
        return res

