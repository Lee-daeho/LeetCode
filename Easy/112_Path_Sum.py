### 112. Path Sum 22/08/11###

###My Solution

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        def DFS(root, val):

            if not root:
                return False

            if not root.left and not root.right and (root.val + val) == targetSum:
                return True

            val += root.val

            return DFS(root.left, val) or DFS(root.right, val)

        return DFS(root, 0)

