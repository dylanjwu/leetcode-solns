class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def build(root, preorder, inorder):
            if preorder == []:
                return None
            
            curr = preorder[0]
            i = inorder.index(curr)
            root.val = curr
            
            root.left = build(TreeNode(), preorder[1:i+1], inorder[:i])
            root.right = build(TreeNode(), preorder[i+1:], inorder[i+1:])
            
            return root
        return build(TreeNode, preorder, inorder)
