from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = None

        while head:
            if not current:
                current = ListNode(head.val)
            else:
                new_node = ListNode(head.val)
                new_node.next = current
                current = new_node

            head = head.next

        return current
