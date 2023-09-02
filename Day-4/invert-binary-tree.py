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
