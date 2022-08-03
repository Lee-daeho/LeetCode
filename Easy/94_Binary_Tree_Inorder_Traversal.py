###94. Binary Tree Inorder Traversal 22/08/03###

###My Solution Recursive -> good

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        else:
            if root.left == None and root.right == None:
                return [root.val]

            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

###More understandable

# recursively
def inorderTraversal1(self, root):
    res = []
    self.helper(root, res)
    return res


def helper(self, root, res):
    if root:
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)


# iteratively
def inorderTraversal(self, root):
    res, stack = [], []
    while True:
        while root:
            #Stack left and right nodes
            stack.append(root)
            #Go to left end
            root = root.left
        if not stack:
            return res
        #Pop the leftest one
        node = stack.pop()
        #Stack leftest value
        res.append(node.val)
        #Because you already done with the left from root, go to the right
        root = node.right