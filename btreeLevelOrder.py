# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = [root]
        
        res = []
        nodes_at_level = 1
        prev_nodes = 1
        while q:
            expected_next_nodes = prev_nodes*2
            front = q.pop(0) 
            print(front.val) 
            res.append(front.val)
            if front.left:
                q.append(front.left)
                nodes_at_level += 1
            if front.right:
                q.append(front.right)
                nodes_at_level += 1
            prev_nodes = nodes_at_level
                    
                
        return res 