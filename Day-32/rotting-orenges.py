import collections
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        self.minute = 0
        visit = set()

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visit.add((r, c))
            
            while q:
                row, col = q.popleft()
                
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                can_elasp = False
                
                for dr, dc in directions:
                    r, c = dr + row, dc + col
                    
                    if (r in range(rows) and 
                        c in range(cols) and 
                        (r, c) not in visit and 
                        grid[r][c] == 1):
                        grid[r][c] = 2
                        q.append((r, c))
                        visit.add((r, c))
                        can_elasp = True
                        
                if can_elasp:
                    self.minute += 1
                
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit and grid[r][c] == 2:
                    bfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return self.minute
    