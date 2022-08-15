### 144. Binary Tree Preorder Traversal 22/08/15###

###My Solution
# Definition for a binary tree node. Similar with 94. Binary Tree Inorder Traversal
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        else:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


###Iterative Solution
def preorderTraversal(self, root):
    stack, res = [root], []
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return res