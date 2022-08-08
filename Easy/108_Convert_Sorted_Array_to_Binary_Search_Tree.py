### 108. Convert Sorted Array to Binary Search Tree 22/08/08 ###

###My solutiona after cheating

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def insert_bst(left, right):        # Need review
            if left == right:
                return None

            mid = (left + right) // 2

            node = TreeNode(nums[mid])

            node.left = insert_bst(left, mid)
            node.right = insert_bst(mid + 1, right)

            return node

        return insert_bst(0, len(nums))