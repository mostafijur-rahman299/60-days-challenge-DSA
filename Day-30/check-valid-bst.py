class Solution:
    def isValidBST(self, root) -> bool:
        def check_BST(root, minimum, maximum):
            if not root: return True
            
            if not(root.val > minimum and root.val < maximum): return False
            
            return check_BST(root.left, minimum, root.val) and check_BST(root.right, root.val, maximum)
            
        return check_BST(root, float("-inf"), float("inf"))
    
    