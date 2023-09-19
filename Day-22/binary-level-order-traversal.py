class Solution:
    def levelOrder(self, root):
        if not root: return []
    
        queue = []
        queue.append(root)
        queue.append(None)
        result = []
        temp_res = []
        
        while queue:
            node = queue.pop(0)
            
            if node is None:
                result.append(temp_res)
                temp_res = []
                if queue:
                    queue.append(None)
                else:
                    break
            else:
                temp_res.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
    
    