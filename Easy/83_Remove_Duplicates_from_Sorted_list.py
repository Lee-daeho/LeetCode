###83. Remove Duplicates from sorted list 22/08/03###


###My Solution -> should think about multiple duplication###
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        new = head

        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        return new


###Recursive solution
def deleteDuplicates(self, head):
    if head and head.next:
        head.next = self.deleteDuplicates(head.next)
        return head.next if head.next.val == head.val else head
    return head