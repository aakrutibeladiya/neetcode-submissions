class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        mlen = len(matrix)
        res = [[0] * mlen for _ in range(mlen)]
        
        for i in range(0,mlen):
            rowcoords = matrix[i]
            j = mlen - i - 1
            for r in range(mlen):
                res[r][j] = rowcoords[r]
        
        for i in range(mlen):
            for j in range(mlen):
                matrix[i][j] = res[i][j]

