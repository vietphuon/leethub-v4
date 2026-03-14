# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.idx = 0
        self.inorder = []
        def dfs(node):
            if not node:
                return

            dfs(node.left)

            # visit
            self.inorder.append(node.val)

            dfs(node.right)
        
        dfs(root)

    def next(self) -> int:
        res = self.inorder[self.idx]
        self.idx += 1
        return res

    def hasNext(self) -> bool:
        # print(self.idx, self.inorder)
        return self.idx < len(self.inorder)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()