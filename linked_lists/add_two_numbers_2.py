# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def calculate_sum_and_carry_over(self, val1, val2, carry_over):
        sum = val1 + val2 + carry_over

        if sum > 9:
            return int(str(sum)[1]), 1
        else:
            return sum, 0

    def add_first(self, value, result):
        temp = ListNode(value)
        temp.next = result
        return temp

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        stack1, stack2 = [], []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        result = None
        carry_over = 0
        last = None

        while len(stack1) > 0 and len(stack2) > 0:
            sum, carry_over = self.calculate_sum_and_carry_over(
                stack1.pop(), stack2.pop(), carry_over
            )

            if result:
                result = self.add_first(sum, result)
            else:
                result = ListNode(sum)

        if len(stack1) > 0:
            for index in range(len(stack1) - 1, -1, -1):
                sum, carry_over = self.calculate_sum_and_carry_over(
                    stack1[index], 0, carry_over
                )
                result = self.add_first(sum, result)

        if len(stack2) > 0:
            for index in range(len(stack2) - 1, -1, -1):
                sum, carry_over = self.calculate_sum_and_carry_over(
                    stack2[index], 0, carry_over
                )
                result = self.add_first(sum, result)

        if carry_over == 1:
            result = self.add_first(carry_over, result)

        return result
