class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Pruning
        board_count = {}
        word_count = {}
        for i in board:
            for j in i:
                if j not in board_count:
                    board_count[j] = 1
                else:
                    board_count[j] += 1
        
        for i in word:
            if i not in word_count:
                word_count[i] = 1
            else:
                word_count[i] += 1
        
        for w in word_count:
            if w not in board_count:
                return False
            if word_count[w] > board_count[w]:
                return False

        # Main DFS
        m = len(board)
        n = len(board[0])
        def dfs(index, left, right):
            if index == len(word): # leaf node
                return True
            if ((left < 0 or left > m-1) or 
            (right < 0 or right > n-1) or 
            board[left][right] != word[index]): # oob or mismatch
                return False
            
            temp = board[left][right]
            board[left][right] = '#'          # mark visited
            
            found = (dfs(index+1, left+1, right) or dfs(index+1, left-1, right) or
                    dfs(index+1, left, right+1) or dfs(index+1, left, right-1))
            
            board[left][right] = temp         # restore (backtrack)
            return found

        res = []
        for i in range(m): 
            for j in range(n):
                if board[i][j] == word[0]: 
                    if dfs(0, i, j):
                        return True
        
        return False
