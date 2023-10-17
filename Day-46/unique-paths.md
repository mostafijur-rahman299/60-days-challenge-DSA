## 62. Unique Paths
```
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that 
the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example:
    Input: m = 3, n = 7
    Output: 28
```


### Solution

```python
res = []
m, n = 3, 7

row = [1] * n

print(row)

for i in range(m-1):
    newRow = [1] * n
    for j in range(n-2, -1, -1):
        newRow[j] = newRow[j+1] + row[j]
    row = newRow    
```

#### Time and Space Complexity Analysis
```
Time Complexity:

    The outer loop iterates m-1 times, where m is the number of rows you want to generate in Pascal's triangle.
    The inner loop iterates from n-2 to 0, which means it goes through n-1 iterations.
    Within the inner loop, basic arithmetic operations are performed (addition and assignment), 
    which are constant-time operations.
    The time complexity of the code can be approximated as O(m * n), where m is the number of rows 
    you want to generate, and n is the number of elements in each row. It's important to note that 
    this is a rough estimate because the actual number of iterations in the inner loop decreases 
    with each iteration of the outer loop.

Space Complexity:

    The code uses two lists, row and newRow, both of size n to store the rows of Pascal's triangle.
    The res list is not used in the code provided, so its space complexity is not considered.
    The space complexity is O(n) because you are creating two lists of size n (i.e., row and newRow) 
    and you are not using any additional data structures that scale with the input.
```
