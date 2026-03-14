# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.prev = None
        self.arr = []

        def dfs(node, idx=0):
            if not node:
                return

            if len(self.arr) < idx + 1:
                self.arr.append([])
            print(self.arr, idx)

            dfs(node.left, idx + 1)

            # visit
            if idx % 2 == 0:
                self.arr[idx].append(node.val)
            else:
                self.arr[idx] = [node.val] + self.arr[idx]

            dfs(node.right, idx + 1)

        dfs(root, 0)
        return self.arr
