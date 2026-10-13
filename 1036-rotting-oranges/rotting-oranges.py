class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        time = 0
        fresh = 0
        rottensCells = []

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    rottensCells.append((row,col))
                elif grid[row][col] == 1:
                    fresh += 1

        moverow = [-1 , 1, 0 , 0]
        movecol = [0 , 0, -1 , 1]

        
        if not fresh :
            return 0
            
            
        while rottensCells:
            newRotten = []
            time += 1
            for item in rottensCells:
                row , col = item[0] ,item[1]
                for i in range(4):
                    newRow = row + moverow[i]
                    newCol = col + movecol[i]

                    if 0 <= newRow < m and 0 <= newCol < n and grid[newRow][newCol] == 1:
                        fresh  -= 1
                        grid[newRow][newCol] = 2
                        newRotten.append((newRow,newCol))
            
            rottensCells = newRotten[:]
        
        return time - 1 if fresh ==  0 else -1