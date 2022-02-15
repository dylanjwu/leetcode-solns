class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        positions = [(0,1), (1,0), (0,-1), (-1, 0)]
        
        
        rows = len(grid)
        cols = len(grid[0])
        
        rottens = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rottens.append((i, j))
                    
        count = -1
        while rottens:
            temp = []
            for i,j in rottens:
                for new_i, new_j in positions:
                    x,y = i+new_i, j+new_j
                    if x >= 0 and x < rows and y >= 0 and y < cols:
                        if grid[x][y] == 1:
                            grid[x][y] = 2
                            temp.append((x, y))
            rottens = temp
            count += 1
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
                
        return 0 if count == -1 else count
