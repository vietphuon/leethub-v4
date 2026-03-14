class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0

        def dfs(r, c):
            # leaf
            if r < 0 or r > m-1 or c < 0 or c > n-1 or grid[r][c] == '0':
                return
            
            # visit
            grid[r][c] = '0'

            # internal
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    # dfs
                    dfs(i, j) # lol like nuking an island and counting each
                    res += 1
        
        return res