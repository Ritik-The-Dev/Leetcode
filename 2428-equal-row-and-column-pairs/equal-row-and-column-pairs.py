class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        
        n = len(grid)

        totalRows = {} 
        totalCols = [""] * n 

        for i , row in enumerate(grid):
            currRow = ",".join(map(str , row))
            totalRows[currRow] = totalRows.get(currRow , 0) + 1 
            
            for x in range(0,n):
                totalCols[x] += ("," if totalCols[x] else "") + str(row[x])
        
        result = 0

        for cols in totalCols:
            if cols in totalRows:
                result += totalRows[cols]
        
        return result