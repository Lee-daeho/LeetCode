### 104. Maximum Depth of Binary Tree 22/08/08###

# My Solution

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if root and (root.left or root.right):
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        else:
            return 1