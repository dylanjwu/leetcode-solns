# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def recurse(root, curr_sum):
                
            if not root:
                return 0

            left = recurse(root.left, curr_sum+root.val)
            right = recurse(root.right, curr_sum+root.val)
            return left+right + int(curr_sum+root.val == targetSum)
        
        
        def dfs(root):
            if not root:
                return 0 
            
            return dfs(root.left)+recurse(root, 0)+dfs(root.right)
        
        return dfs(root)
