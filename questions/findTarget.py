from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        stack = [root]
        sum_dict = {}

        while stack:

            node = stack.pop(0)

            if node.val in sum_dict.keys():
                return True
            else:
                sum_dict[k - node.val] = node.val

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return False
