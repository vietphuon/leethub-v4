class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        self.arr = [[] for i in range(m + n)]
        for i in range(m):
            for j in range(n):
                diag = i + j
                if diag % 2 == 0:
                    self.arr[diag] = [mat[i][j]] + self.arr[diag]
                else:
                    self.arr[diag].append(mat[i][j])
        
        res = []
        for i in self.arr:
            res += i
        return res