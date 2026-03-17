# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(node, max_val):
            # leaf
            if not node:
                return
            
            if node.val >= max_val:
                max_val = node.val
                self.count += 1
            
            # visit

            # node
            dfs(node.left, max_val)
            dfs(node.right, max_val)
        
        dfs(root, 0)

        return self.count