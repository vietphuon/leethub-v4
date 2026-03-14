class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        visit = matrix[0][0] - 1
        def dfs(r, c):
            print(r, c)
            # leaf
            if r >= m or c >= n or matrix[r][c] == visit or matrix[r][c] > target:
                return False
            if matrix[r][c] == target:
                return True
            
            # visit
            matrix[r][c] = visit

            # node
            return dfs(r+1, c) or dfs(r, c+1)
        
        return dfs(0, 0)