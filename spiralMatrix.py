class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def recurse(dir,x1,x2,y1,y2):
            if x1 > x2 or y1 > y2:
                return []

            if dir == 'R':
                l = matrix[y1][x1:x2+1]
                y1 += 1
                dir = 'D'
            elif dir == 'L':
                l = matrix[y2][x1:x2+1][::-1]
                y2 -= 1 
                dir = 'U'
            elif dir == 'D':
                l = [matrix[i][x2] for i in range(y1, y2+1)]
                x2 -= 1
                dir = 'L'
            else:
                l = [matrix[i][x1] for i in range(y1, y2+1)][::-1]
                x1 += 1
                dir = 'R'

            return l + recurse(dir, x1, x2, y1, y2)
        
        return recurse('R', 0, len(matrix[0])-1, 0, len(matrix)-1)
