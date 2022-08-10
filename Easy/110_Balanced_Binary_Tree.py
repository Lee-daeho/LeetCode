### 110. Balanced Binary Tree 22/08/10 ###

#My Solution -> it is important to save False value if it have been seen once

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left_node = root.left
        right_node = root.right

        def DFS(root):

            if not root:
                return 1

            else:
                d = max(DFS(root.left) + 1, DFS(root.right) + 1)
                l_depth = DFS(root.left)
                r_depth = DFS(root.right)

                if not l_depth or not r_depth or abs(l_depth - r_depth) > 1:
                    return False
                else:
                    return max(l_depth + 1, r_depth + 1)

        l_depth = DFS(left_node)
        r_depth = DFS(right_node)

        if not l_depth or not r_depth or abs(l_depth - r_depth) > 1:
            return False
        else:
            return True