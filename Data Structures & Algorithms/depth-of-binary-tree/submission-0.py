# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # using recursive approach 
        #if root has no child return 0
        
        if not root:
            return 0
        
        #return 1 if (max(dfs(left subtree), dfs(right subtree))
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))