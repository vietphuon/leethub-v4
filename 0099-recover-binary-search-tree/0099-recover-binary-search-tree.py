# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = self.second = self.prev = None

        node = root
        # Morris Traversal
        # if node.left is None:
        #     → no left subtree, visit current, go right

        # else:
        #     → find inorder predecessor (rightmost of left subtree)
            
        #     if predecessor.right is None:
        #         → first visit: CREATE the thread (predecessor.right = node)
        #         → go left
            
        #     if predecessor.right == node:
        #         → second visit: REMOVE the thread (predecessor.right = None)
        #         → visit current node ← this is where you check violations
        #         → go right
        while (node):
            if not node.left:
                # visit = check violation
                if self.prev and self.prev.val > node.val:
                    if not self.first:
                        self.first = self.prev
                    self.second = node
                
                self.prev = node
                node = node.right
            else:
                pred = node.left
                while pred.right and pred.right != node:
                    pred = pred.right
                
                if not pred.right:
                    pred.right = node
                    node = node.left
                else:
                    pred.right = None

                    # visit = check violation
                    if self.prev and self.prev.val > node.val:
                        if not self.first:
                            self.first = self.prev
                        self.second = node
                    
                    self.prev = node
                    node = node.right
        
        self.first.val, self.second.val = self.second.val, self.first.val

    def recoverTree1(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = self.second = self.prev = None

        def inorder(node):
            # standard inorder: left → process → right
            # when prev.val > node.val, record first/second

            # start inorder traversal
            #     at each node:
            #         compare prev vs current node
            #         if prev.val > curr.val → record violation
            #         update prev = current node
            #         continue right
            if not node:
                return
            
            inorder(node.left)

            # visit = check violation
            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                self.second = node
            
            self.prev = node
            
            inorder(node.right)

        inorder(root)

        self.first.val, self.second.val = self.second.val, self.first.val
        