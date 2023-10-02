import collections
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time, fresh = 0, 0
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    q.append((row, col))

        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        while q and fresh > 0:
            for q_index in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r < 0 or r == len(grid) or
                    c < 0 or c == len(grid[0]) or
                    grid[r][c] != 1):
                        continue
                        
                    grid[r][c] = 2
                    q.append((r, c))
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1