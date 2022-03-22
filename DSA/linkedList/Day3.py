from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1->2->3->4->N
# 0p  4->3->-2->1->N

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current is not None:
            tempNode = current.next
            current.next = prev
            prev = current
            current = tempNode
        return prev

    # Find middle of the linked List
    # Approach-1 get the length of the List and then find mid= length/2

    def middleOfLL(self, head):
        length = 0
        current = head

        while current is not None:
            length += 1
            current = current.next

        current = head
        mid = length // 2
        for i in range(0, mid):
            current = current.next
        return current

    # Approach-2 by using slow and Fast pointer

    def middleOfLL(self, head):
        slowPtr = head
        fastPtr = head

        while fastPtr.next and fastPtr.next.next:
            fastPtr = fastPtr.next.next
            slowPtr = slowPtr.next

        if fastPtr.next:
            return slowPtr.next
        else:
            return slowPtr
