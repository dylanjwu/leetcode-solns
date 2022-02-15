# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isBST(root, minn, maxx):
            if not root:
                return True

            if root.val <= minn or root.val >= maxx:
                return False
            
            return isBST(root.left, minn, root.val) and isBST(root.right, root.val, maxx)
        
        return isBST(root, -sys.maxsize, sys.maxsize)
