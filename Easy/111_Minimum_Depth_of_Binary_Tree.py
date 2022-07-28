### 111. Minimum Depth of Binary Tree 22/07/28 ###

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

###My Solution of DFS after cheating (recursive)
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if root.right and not root.left:
            return self.minDepth(root.right) + 1

        if root.left and not root.right:
            return self.minDepth(root.left) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

###My Solution of BFS after cheating (queue)
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        from collections import deque

        queue = deque([(root, 1)])

        while queue:
            node, level = queue.popleft()

            if node:
                if not node.left and not node.right:
                    return level
                else:
                    queue.append((node.left, level + 1))
                    queue.append((node.right, level + 1))