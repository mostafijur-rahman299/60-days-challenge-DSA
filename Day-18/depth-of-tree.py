class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def build_tree_with_level_order(array):
    queue = []
    root = Node(array[0])
    queue.append(root)
    
    index = 1
    
    while queue and index < len(array):
        node = queue.pop(0)
        if array[index]:
            node.left = Node(array[index])
            queue.append(node.left)
        index += 1
        
        if array[index]:
            node.right = Node(array[index])
            queue.append(node.right)
        index += 1
    return root
        
def traverse(root):
    queue = []
    queue.append(root)
    
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
            
        
array = [1, None,15]
root = build_tree_with_level_order(array)
traverse(root)
height(root)
