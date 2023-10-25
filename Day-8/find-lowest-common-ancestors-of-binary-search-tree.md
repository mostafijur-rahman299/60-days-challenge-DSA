## 235. Lowest Common Ancestor of a Binary Search Tree

```
Given a binary search tree (BST), find the lowest common ancestor (LCA) 
node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor 
is defined between two nodes p and q as the lowest node in T that has both p and q 
as descendants (where we allow a node to be a descendant of itself).”

Example:
    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
    Output: 6
```

### Solution 01 (While Loop)

```python
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    pv=p.val
    qv=q.val
    while(root!=None):
        if pv <root.val and qv<root.val:
            root=root.left
        elif pv>root.val and qv>root.val:
            root=root.right
        else:
            return root
    return root
```
#### Time & Space Complexity Analysis
```
Time Complexity:
    The time complexity of this code is O(h), where "h" is the height of the BST. 
    In the worst case, if the tree is completely unbalanced (essentially a linked list), 
    the height of the tree is O(n), where "n" is the number of nodes in the tree. In the best case, 
    when the tree is balanced, the height is O(log n) for a tree with "n" nodes.

Space Complexity:
    The space complexity of this code is O(1). It uses a constant amount of extra space 
    for the pv and qv variables and does not use any additional data structures that scale 
    with the input size. The space complexity is not dependent on the size of the tree.


```


### Solution 02 (Recursive)
```python
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    pv=p.val
    qv=q.val
    def lowest_common_anchestor(root):  
        if not root: return

        if pv > root.val and qv > root.val:
            root = lowest_common_anchestor(root.right)
        elif pv < root.val and qv < root.val:
            root = lowest_common_anchestor(root.left)
        
        return root
    return lowest_common_anchestor(root)
```

#### Time & Space Complexity Analysis
```
Time Complexity:
    The time complexity of this code is O(h), where "h" is the height of the BST. 
    In the worst case, if the tree is completely unbalanced (essentially a linked list), 
    the height of the tree is O(n), where "n" is the number of nodes in the tree. In the best case, 
    when the tree is balanced, the height is O(log n) for a tree with "n" nodes.

Space Complexity:
    The space complexity of this code is O(h), where "h" is the height of the BST, 
    and it is determined by the maximum depth of the recursion stack. In the worst case, 
    with an unbalanced tree, the space complexity is O(n), where "n" is the number of nodes. 
    In the best case with a balanced tree, the space complexity is O(log n).
```
