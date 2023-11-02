"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return None

        queue = []
        queue.append(root)
        level = 0

        while queue:
            number_of_items_needed = 2**level

            if len(queue) == number_of_items_needed:
                for index, item in enumerate(queue):
                    if index + 1 < len(queue):
                        item.next = queue[index + 1]
                    else:
                        item.next = None
                level += 1
            else:
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return root
