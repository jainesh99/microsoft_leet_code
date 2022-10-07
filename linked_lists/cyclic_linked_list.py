# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head:
            return False

        if not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:

            if fast is None or fast.next is None:
                return False

            slow = slow.next
            fast = fast.next.next

        return True


# This can also be done with a dictionary, where you can store the memory address and check that...
