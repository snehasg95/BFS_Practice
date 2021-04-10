# with size variable

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        
        if not grid or len(grid) == 0:
            return -1
        
        rows = len(grid)
        cols = len(grid[0])
        
        queue = collections.deque()
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '*':
                    queue.append((i,j))
                    
        
        distance = 1
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        while queue:
            
            
            size = len(queue)
            for i in range(size):
                
                cr, cc = queue.popleft()
                
                for dir in dirs:
                    r = cr + dir[0]
                    c = cc + dir[1]
                    
                    if r >= 0 and r < rows and c >= 0 and c < cols and grid[r][c] != 'X':
                        
                        if grid[r][c] == '#':
                            return distance
                        
                        if grid[r][c] == 'O':
                            grid[r][c] = distance
                            queue.append((r,c))
                            
            distance += 1
                            
                
        return -1
                
                
  # without  size variable we can include distance in queue as well

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        
        if not grid or len(grid) == 0:
            return -1
        
        rows = len(grid)
        cols = len(grid[0])
        distance = 1
        queue = collections.deque()
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '*':
                    grid[i][j] = 'X'
                    queue.append((i,j, distance))
                    
        
        
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        while queue:
            
            
            # size = len(queue)
            # for i in range(size):
                
            cr, cc, distance = queue.popleft()

            for dir in dirs:
                r = cr + dir[0]
                c = cc + dir[1]
                

                if r >= 0 and r < rows and c >= 0 and c < cols and grid[r][c] != 'X':

                    if grid[r][c] == '#':
                        return distance

                    if grid[r][c] == 'O':
                        grid[r][c] = distance + 1 # visited
                        queue.append((r,c, distance + 1))
                            
            # distance += 1
                            
                
        return -1
                
                
        
