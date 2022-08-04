### 2. Add Two Numbers 22/08/04 ###

###My Solution failed to optimize but works well

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        cur = sums = ListNode(0)

        while l1 and l2:
            nxt = l1.val + l2.val + carry

            sums.next = ListNode(nxt % 10)

            l1 = l1.next
            l2 = l2.next
            sums = sums.next

            carry = nxt // 10

        while carry:
            if not l1 and not l2:
                sums.next = ListNode(carry)

                carry = 0

            elif l1:
                nxt = l1.val + carry
                sums.next = ListNode(nxt % 10)

                carry = nxt // 10

                l1 = l1.next


            else:
                nxt = l2.val + carry
                sums.next = ListNode(nxt % 10)

                carry = nxt // 10

                l2 = l2.next
            sums = sums.next

        sums.next = l1 or l2

        return cur.next


### concise and same solution

 def addTwoNumbers(self, l1, l2):
        carry = 0;
        res = n = ListNode(0);
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next;
            if l2:
                carry += l2.val;
                l2 = l2.next;
            carry, val = divmod(carry, 10)
            n.next = n = ListNode(val);
        return res.next;