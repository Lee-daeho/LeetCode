### 145. Binary Tree Postorder Traversal 22/08/15###

###My Solution

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        else:
            return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

###My iterative solution : tricky solution from discuss. Because postorder traversal goes left->right->mid, save in res as mid->right->left order and reverse it
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        stack = [root]
        res = []

        while stack:
            node = stack.pop()

            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

        return res[::-1]