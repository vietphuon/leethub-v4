class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [["_" for i in range(3)] for i in range(3)]

        for idx, (i, j) in enumerate(moves):
            if idx % 2 == 0:
                board[i][j] = 'A'
            else:
                board[i][j] = 'B'
        
        def win(player: str):
            for i in range(3):
                # row
                if all(board[i][j] == player for j in range(3)):
                    return player
                # col
                if all(board[j][i] == player for j in range(3)):
                    return player
            
            # diag1
            if all(board[i][i] == player for i in range(3)):
                return player
            
            # diag2
            if all(board[2 - i][i] == player for i in range(3)):
                return player
        print(board)
        if win('A'):
            return 'A'
        if win('B'): 
            return 'B'
        if len(moves) == 9:
            return 'Draw'
        else:
            return 'Pending'