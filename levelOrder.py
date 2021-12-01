"""
I originally tried to solve this using BFS. While that is certainly a viable option, I found using DFS much more straightforward.
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        def helper(root, depth):
            if not root:
                return 
            
            if len(res) > depth:
                res[depth].append(root.val)
            else:
                res.append([root.val])
                
            for child in root.children:
                helper(child, depth+1)
        
        res = []
        helper(root, 0)
        return res
      
