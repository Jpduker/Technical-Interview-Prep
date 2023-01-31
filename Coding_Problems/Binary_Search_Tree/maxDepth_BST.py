def maxDepth(self, root: Optional[TreeNode]) -> int:
    if root ==None:
        return 0
    left_subtree = self.maxDepth(root.left)
    right_subtree = self.maxDepth(root.right)
    
    return 1+ max(left_subtree,right_subtree)