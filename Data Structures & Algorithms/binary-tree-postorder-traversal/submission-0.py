class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        visit = [False]
        res = []

        while stack:
            cur, v = stack.pop(), visit.pop()
            
            if cur:
                if v:
                    # If we have visited this root node's children already, process its value
                    res.append(cur.val)
                else:
                    # First time seeing this node: push it back with visit=True
                    stack.append(cur)
                    visit.append(True)
                    
                    # Push right child with visit=False
                    stack.append(cur.right)
                    visit.append(False)
                    
                    # Push left child with visit=False
                    stack.append(cur.left)
                    visit.append(False)
                    
        return res