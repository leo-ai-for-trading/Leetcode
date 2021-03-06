class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        perimeter = 0
        for r in range(row):
            for c in range(col):
                adj_land = 0
                if grid[r][c] == 1:
                    for d in directions:
                        ro = r + d[0]
                        co = c + d[1]
                        if 0 <= ro < row and 0 <= co < col and grid[ro][co] == 1:
                            adj_land += 1
                    perimeter += (4 - adj_land)
        return perimeter
