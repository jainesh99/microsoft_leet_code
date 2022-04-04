from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        length_of_ll = 1
        current = head

        while current != None:
            current = current.next
            length_of_ll += 1

        last_index = length_of_ll - k

        current = head
        traverser = 1

        while traverser != k:
            current = current.next
            traverser += 1

        first_item_to_swap = current

        current = head

        traverser = 1

        while traverser != last_index:
            current = current.next
            traverser += 1

        last_item_to_swap = current

        temp = first_item_to_swap.val
        first_item_to_swap.val = last_item_to_swap.val
        last_item_to_swap.val = temp

        return head
