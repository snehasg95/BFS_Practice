class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        if not grid:
            return -1
        
        rows = len(grid)
        cols = len(grid[0])
        
        # destination
        target_row = rows - 1
        target_col = cols - 1
        
        # edge case
        if grid[0][0] != 0 or grid[target_row][target_col] != 0:
            return -1
        
        queue = deque()
        # append r, c, moves, k
        queue.append((0,0,0,k))
        
        visited = set()
        visited.add((0,0,k))
        
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        
        while queue:
            
            cr, cc, moves, obst = queue.popleft()
            if (cr, cc) == (target_row, target_col):
                return moves

            for dir in dirs:
                nr = cr + dir[0]
                nc = cc + dir[1]

                if nr >= 0 and nr < rows and nc >= 0 and nc < cols and (nr,nc,obst) not in visited:
                    
                    if grid[nr][nc] == 0:
                        visited.add((nr,nc,obst))
                        queue.append((nr, nc, moves + 1, obst))

                    elif grid[nr][nc] == 1 and obst > 0:
                        visited.add((nr,nc,obst))
                        # decrement obstacle permissible count
                        queue.append((nr, nc, moves + 1, obst-1))
                        

            
        return -1
                        
                    
                    
                
# For large tc's we could use manhattan distance and skip all these
# if (k >= grid.length + grid[0].length - 3) {
#           return grid.length + grid[0].length - 2;
#       }
        
