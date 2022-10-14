# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def carry_over(self, result):

        if result > 9:
            result = int(str(result)[1])
            return result, 1
        else:
            return result, 0

    def traverse_list(self, l3):

        temp = l3

        while temp.next:
            temp = temp.next

        return temp

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        sum = None
        carry_over = 0

        while l1 != None:

            if l2:
                result = l1.val + l2.val + carry_over

                result, carry_over = self.carry_over(result)

                if sum:
                    temp = self.traverse_list(sum)
                    temp.next = ListNode(result)
                else:
                    sum = ListNode(result)
            else:
                break

            l1 = l1.next
            l2 = l2.next

        if l1:

            while l1 != None:
                result = l1.val + carry_over
                result, carry_over = self.carry_over(result)
                temp = self.traverse_list(sum)
                temp.next = ListNode(result)
                l1 = l1.next
        elif l2:

            while l2 != None:
                result = l2.val + carry_over
                result, carry_over = self.carry_over(result)
                temp = self.traverse_list(sum)
                temp.next = ListNode(result)
                l2 = l2.next

        if carry_over == 1:
            temp = self.traverse_list(sum)
            temp.next = ListNode(carry_over)

        return sum
