### 19. Remove Nth Node From End of List 22/09/02

###My Solution
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head.next:
            return None

        slow = fast = head
        gap = 0

        while fast.next:
            fast = fast.next
            gap += 1
            if gap > n:
                slow = slow.next

        if gap >= n:
            slow.next = slow.next.next
        else:
            head = head.next

        return head
