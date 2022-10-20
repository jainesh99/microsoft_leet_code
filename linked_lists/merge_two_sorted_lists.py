# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_last(self, head, last, value):

        if not head:
            head = ListNode(value)
            last = head
        else:
            last.next = ListNode(value)
            last = last.next

        return head, last

    def move_next(self, head):

        try:
            head = head.next
            value = head.val
        except Exception:
            head = None
            value = None

        return head, value

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        head, last = None, None
        val1, val2 = None, None

        if list1:
            val1 = list1.val

        if list2:
            val2 = list2.val

        while list1 or list2:

            if val1 is not None and val2 is not None:

                if val1 > val2:
                    head, last = self.add_last(head, last, val2)
                    list2, val2 = self.move_next(list2)
                else:
                    head, last = self.add_last(head, last, val1)
                    list1, val1 = self.move_next(list1)

            elif val1 is not None:
                head, last = self.add_last(head, last, val1)
                list1, val1 = self.move_next(list1)
            elif val2 is not None:
                head, last = self.add_last(head, last, val2)
                list2, val2 = self.move_next(list2)

        return head
