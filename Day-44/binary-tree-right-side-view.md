199. Binary Tree Right Side View
```
Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom

Example:
    Input: root = [1,2,3,null,5,null,4]
    Output: [1,3,4]
```

### Solution
```python
def level_order_travarse(root):
    res = []
    queue = [root]
    
    while queue:
        rightSide = None
        qLen = len(queue)
        
        for i in range(qLen):
            node = queue.pop(0)
            if node:
                rightSide = node
                queue.append(node.left)
                queue.append(node.right)
        
        if rightSide:
            res.append(rightSide.val)
            
    return res
```

#### Time Complexity analysis
```
The code uses a while loop to traverse the tree level by level. In the worst case, the loop will run for all nodes in the tree.
For each node, you are doing constant time operations (e.g., appending to the queue, popping from the queue).
Therefore, the time complexity of this code is O(n), where n is the number of nodes in the binary tree.
```
#### Space complexity analysis
```
The space complexity is determined by the space used for the queue and the res list.
The queue will store nodes at each level, and at its peak, it will contain nodes from one level of the tree. So, at most, it can contain all the nodes from one level of the tree.
In the worst case, if the tree is perfectly balanced, the number of nodes in a level will be approximately n/2.
Therefore, the space complexity is O(n/2), which simplifies to O(n).
```
