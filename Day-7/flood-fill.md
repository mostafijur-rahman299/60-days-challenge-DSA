## 733. Flood Fill

```
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

Example:
    Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
    Output: [[2,2,2],[2,2,0],[2,0,1]]
```


### Solution

```python
from typing import List

def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    ROWS, COLS = len(image), len(image[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    oldColor = image[sr][sc]
    
    def dfs(row, col):
        if (row < 0 or row >= ROWS or 
            col < 0 or col >= COLS or 
            image[row][col] != oldColor or 
            image[row][col] == newColor):
            return
        
        image[row][col] = newColor
        
        for rowOffset, colOffset in directions:
            newRow = row + rowOffset
            newCol = col + colOffset
            dfs(newRow, newCol)
        
    dfs(sr, sc)
    return image
```

#### Time & Space Complexity Analysis
```
Time Complexity:
    The time complexity of this code is O(N), where N is the total number of cells in the grid. 
    This is because in the worst case, the DFS algorithm will visit each cell once to determine 
    if it should be changed and, if necessary, change its color. The DFS explores all connected 
    cells in a region, but each cell is visited at most once. So, for an MxN grid, the time 
    complexity is O(M * N).

Space Complexity:
    The space complexity of this code is O(M * N), which corresponds to the maximum space required by 
    the call stack during the depth-first search. In the worst case, if the entire grid is part of 
    the same region and the DFS traverses from one corner to the other, the call stack could reach 
    a depth of M * N, where M is the number of rows and N is the number of columns. Each recursive 
    call consumes a constant amount of space (for function call context), and since there can be 
    M * N recursive calls in the worst case, the space complexity is O(M * N).

```
