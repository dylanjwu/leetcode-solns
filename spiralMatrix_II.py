class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        matrix = [[0]*n for _ in range(n)]
        num = 1
        
        x_lo, x_hi = 0, n-1 
        y_lo, y_hi = 0, n-1
        
        DIR = 'R'
        
        while num <= n**2:
            
            if DIR == 'R':
                for i in range(x_lo, x_hi+1):
                    matrix[y_lo][i] = num
                    num += 1
                y_lo += 1
                DIR = 'D'
                
            elif DIR == 'D':
                for j in range(y_lo, y_hi+1):
                    matrix[j][x_hi] = num
                    num += 1
                x_hi -= 1
                DIR = 'L'
                
            elif DIR == 'L':
                for k in range(x_hi, x_lo-1, -1):
                    matrix[y_hi][k] = num
                    num += 1
                y_hi -= 1 
                DIR = 'U'
                
            else: # DIR == 'U'
                for l in range(y_hi, y_lo-1, -1):
                    print(l)
                    matrix[l][x_lo] = num
                    num += 1
                x_lo += 1
                DIR = 'R' 
        return matrix
                    
