## 110. Balanced Binary Tree
```
Given a binary tree, determine if it is height-balanced

Example:
    Input: root = [3,9,20,null,null,15,7]
    Output: true
```

### Solution (DFS)

```python
class Solution(object):
    def isBalanced(self, root):
        return (self.Height(root) >= 0)
    
    def Height(self, root):
        if root is None:  return 0
        leftheight, rightheight = self.Height(root.left), self.Height(root.right)
        if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:  return -1
        return max(leftheight, rightheight) + 1
```

#### Time & Space Complexity Analysis
```
Time Complexity:
    The code uses a depth-first traversal approach to calculate the height of the binary tree. 
    It visits each node once, and for each node, it performs some constant time operations. 
    Therefore, the time complexity is O(n), where 'n' is the number of nodes in the binary tree. 
    In the worst case, the code needs to visit every node in the tree to determine its height 
    and check if it's balanced.

Space Complexity:
    The space complexity is determined by the recursive calls and the call stack space used during 
    the recursive traversal. In the worst case, the code can have at most O(h) function calls on 
    the call stack, where 'h' is the height of the tree. Therefore, the space complexity is O(h).

    It's important to note that the space complexity depends on the height of the tree rather than 
    the number of nodes. In a balanced binary tree, the height is O(log n), where 'n' is 
    the number of nodes, resulting in a space complexity of O(log n). However, in the worst case, 
    where the tree is completely unbalanced (e.g., a linked list), the height is O(n), 
    resulting in a space complexity of O(n).

```
