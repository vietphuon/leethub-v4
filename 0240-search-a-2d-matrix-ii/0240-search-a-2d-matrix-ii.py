class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        def dfs(r, c):
            # print(r, c)
            # leaf
            if r >= m or c >= n or not matrix[r][c] or matrix[r][c] > target:
                return False
            if matrix[r][c] == target:
                return True
            
            # visit
            matrix[r][c] = 0

            # node
            return dfs(r+1, c) or dfs(r, c+1)
        
        return dfs(0, 0)