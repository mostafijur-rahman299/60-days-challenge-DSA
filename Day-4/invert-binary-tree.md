## 226. Invert Binary Tree
```
Given the root of a binary tree, invert the tree, and return its root.

Example:
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]
```

### Solution
```python
# build preorder tree by array
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def build_preorder_tree(arr):
    if not arr:
        return
    
    item = arr.pop(0)
    if item == -1:
        return None
    
    node = TreeNode(item)
    node.left = build_preorder_tree(arr)
    node.right = build_preorder_tree(arr)
    
    return node


def traversal(root):
    queue = []
    data = []
    
    queue.append(root)
    
    while queue:
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
        data.append(node.val)
        
    print(data)
    

def invertTree(root):
    if not root:
        return
    
    root.left, root.right = root.right, root.left
    
    invertTree(root.left)
    invertTree(root.right)
    return root


arr = [4, 2, 1, -1, -1, 3, -1, -1, 7, 6, -1, -1, 9, -1, -1]
tree = build_preorder_tree(arr)

traversal(tree)

invert_tree = invertTree(tree)

traversal(invert_tree)
```


#### Time & Space Complexity Analysis
```
Time Complexity:
    Each node is processed once to swap its left and right children.
    The code then recursively calls invertTree on the left and right subtrees, 
    but each node is processed only once in each recursive call.
    Therefore, the time complexity is O(n), where 'n' is the number of nodes in the tree.

Space Complexity:
    The space complexity of this code is determined by the recursion stack. 
    In the worst case, if the binary tree is completely unbalanced and resembles a linked list (skewed tree), 
    the space complexity could be O(n) as there would be n recursive calls on the stack. However, 
    in a balanced binary tree, the space complexity would be closer to O(log n), where 'log n' is the height of the tree.

    In summary, the space complexity is O(h), where 'h' is the height of the binary tree. 
    In the average case for a balanced tree, it's O(log n), but in the worst case for a skewed tree, it's O(n).

    Keep in mind that the space complexity is determined by the depth of the recursion, 
    which is based on the height of the binary tree, and not the size of the input data.
```
