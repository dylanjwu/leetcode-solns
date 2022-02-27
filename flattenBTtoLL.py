# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
            
        if not (root.left or root.right):
            return root
        
        right = self.flatten(root.right)
        left = self.flatten(root.left) 
        
        root.right = left
        
        left_node = root.right
        
        if left_node:
            while left_node.right:
                left_node = left_node.right
            left_node.right = right
        else:
            root.right = right
            
        root.left = None
        
        return root
        
