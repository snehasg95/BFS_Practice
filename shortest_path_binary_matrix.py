class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0
        
        queue = deque()
        
        rows = len(grid)
        cols = len(grid[0])
        
        dest_row = rows - 1
        dest_col = cols - 1

        # base case, if first index and last are not 0 we cannot reach destination
        if grid[0][0] != 0 or grid[dest_row][dest_col] != 0:
            return -1
        
        grid[0][0] = 1 # mark visited
        moves = 1
        queue.append((0,0, moves))  

        # 8 dirs
        dirs = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1, 1), (-1,-1)]
        
        
        while queue:
        
            cr, cc, moves = queue.popleft()
           
            # is it the destination already?
            if cr == dest_row and cc == dest_col:
                return moves
            # if not explore other 8 dirs
            for dir in dirs:
                nr = cr + dir[0]
                nc = cc + dir[1]

                if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == 0:
                    # mark visited in terms of distance
                    grid[nr][nc] = 1
                    queue.append((nr,nc, moves + 1))

            
        return -1
              
        
        
# Instead of moves we can also mutate grid with distance itself and return it

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0
        
        queue = deque()
        
        rows = len(grid)
        cols = len(grid[0])
        
        dest_row = rows - 1
        dest_col = cols - 1

        # base case, if first index and last are not 0 we cannot reach destination
        if grid[0][0] != 0 or grid[dest_row][dest_col] != 0:
            return -1
        
        grid[0][0] = 1 # mark visited
    
        queue.append((0,0))  

        # 8 dirs
        dirs = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1, 1), (-1,-1)]
        
        
        while queue:
        
            cr, cc = queue.popleft()
            distance = grid[cr][cc]          
            # is it the destination already?
            if cr == dest_row and cc == dest_col:
                return distance
            # if not explore other 8 dirs
            for dir in dirs:
                nr = cr + dir[0]
                nc = cc + dir[1]

                if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == 0:
                    # mark visited in terms of distance, update as distance
                    grid[nr][nc] = distance + 1 
                    queue.append((nr,nc))

            
        return -1
                        

            

            
