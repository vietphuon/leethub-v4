class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        res = []

        # build trie
        trie = {}
        for word in words:
            curr = trie # pointer / reference
            for char in word:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]

            curr['$'] = word
        
        # print(trie)
        
        def dfs(r, c, curr=trie):
            # leaf
            if r >= m or r < 0 or c >=n or c < 0 or board[r][c] == '#' or board[r][c] not in curr:
                return

            char = board[r][c]
            nxt = curr[char]
            
            if '$' in nxt:
                res.append(nxt['$'])
                del nxt['$']

            # visited
            board[r][c] = '#'

            # next node
            dfs(r+1, c, nxt)
            dfs(r, c+1, nxt)
            dfs(r-1, c, nxt)
            dfs(r, c-1, nxt)
            
            board[r][c] = char

        for i in range(m):
            for j in range(n):
                dfs(i, j)
        return res
    
    def findWords1(self, board: List[List[str]], words: List[str]) -> List[str]: # Timelimit
        m, n = len(board), len(board[0])
        res = []
        
        def dfs(r, c, curr=''):
            # leaf
            if curr in words and curr not in res:
                res.append(curr)
            if r >= m or r < 0 or c >=n or c < 0 or board[r][c] == '#':
                return
            
            # visited
            char = board[r][c]
            board[r][c] = '#'

            # next node
            dfs(r+1, c, curr+char)
            dfs(r, c+1, curr+char)
            dfs(r-1, c, curr+char)
            dfs(r, c-1, curr+char)
            
            board[r][c] = char

        for i in range(m):
            for j in range(n):
                dfs(i, j)
        return res