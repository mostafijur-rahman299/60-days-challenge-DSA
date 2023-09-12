class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def build_tree_level_order(array):
    queue = []
    root = Node(array.pop(0))
    queue.append(root)
    
    while queue:
        node = queue.pop(0)
        if array:
            node.left = Node(array.pop(0))
            node.right = Node(array.pop(0))
            
            queue.append(node.left)
            queue.append(node.right)
    return root

def level_order_traverse(root):
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.val, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            

def height(root):
    if not root: return 0
    return max(height(root.left), height(root.right)) + 1

def diameter(root):
    if not root: return 0
    
    diameter1 = diameter(root.left)
    diameter2 = diameter(root.right)
    diameter3 = height(root.left) + height(root.right) + 1
    
    return max(diameter3, max(diameter1, diameter2))
    
            
array = [1,2,3,4,5]
tree = build_tree_level_order(array)
level_order_traverse(tree)

height(tree)

