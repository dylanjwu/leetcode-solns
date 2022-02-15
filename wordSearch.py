class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        
        ROWS = len(board)
        COLS = len(board[0])
        WORD_LEN = len(word)
        
        def dfs(i, j, word_len):
            
            if word_len == WORD_LEN: return True
        
            if 0 > i or i >= ROWS: return False
            if 0 > j or j >= COLS: return False
            if word[word_len] != board[i][j]: return False
            if (i, j) in visited: return False
            
            word_found = False
            visited.add((i, j))
            
            for next_i, next_j in neighbors:
                row, col = i+next_i, j+next_j
                word_found = word_found or dfs(row, col, word_len+1)
            visited.remove((i, j))
            
            return word_found
            
              
        
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True
        return False
