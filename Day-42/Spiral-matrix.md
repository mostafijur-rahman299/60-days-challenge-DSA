


### Solution
```python
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9],
          [10,11,12]
        ]


direction, top, left, right, down = 0, 0, 0, len(matrix[0])-1, len(matrix)-1
result = []

while top <= down and left <= right:
    if direction == 0:
        for i in range(left, right+1):
            result.append(matrix[top][i])
        top += 1
        
    elif direction == 1:
        for i in range(top, down+1):
            result.append(matrix[i][right])
        right -= 1
        
    elif direction == 2:
        for i in range(right, left-1, -1):
            result.append(matrix[down][i])
        down -= 1
        
    elif direction == 3:
        for i in range(down, top-1, -1):
            result.append(matrix[i][left])
        left += 1
            
    direction = (direction + 1) % 4
    
print(result)
```

