###101. Symmetric Tree 22/08/08###

###My Solution recursive

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left_node = root.left
        right_node = root.right

        return self.isTrue(left_node, right_node)

    def isTrue(self, left, right):

        if left and right:
            return left.val == right.val and self.isTrue(left.right, right.left) and self.isTrue(left.left, right.right)

        else:
            return left == right

###Stack based iterative Solution

 class Solution2:
  def isSymmetric(self, root):
    if root is None:
      return True

    stack = [[root.left, root.right]]

    while len(stack) > 0:
      pair = stack.pop(0)
      left = pair[0]
      right = pair[1]

      if left is None and right is None:
        continue
      if left is None or right is None:
        return False
      if left.val == right.val:
        stack.insert(0, [left.left, right.right])

        stack.insert(0, [left.right, right.left])
      else:
        return False
    return True