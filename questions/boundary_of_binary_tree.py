from collections import defaultdict, deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        # level_order_queue = deque([root, None])
        # level_dict = defaultdict(list)
        # level = 0
        # boundary = []
        #
        # while level_order_queue:
        #
        #     current_node = level_order_queue.popleft()
        #
        #     if current_node:
        #         level_dict[level].append(current_node.val)
        #
        #         if current_node.left:
        #             level_order_queue.append(current_node.left)
        #         if current_node.right:
        #             level_order_queue.append(current_node.right)
        #
        #     else:
        #         level += 1
        #
        #         if len(level_order_queue) > 0:
        #             level_order_queue.append(None)
        #
        # for level in range(len(level_dict) - 1):
        #     boundary.append(level_dict[level][0])
        #
        # boundary = boundary + level_dict[len(level_dict)-1]
        #
        # for level in range(len(level_dict) - 2, 0, -1):
        #     boundary.append(level_dict[level][len(level_dict[level])-1])
        #
        # return boundary

        left, leaves, right = [], [], []

        def add_left(node):
            if not node:
                return
            if node.left or node.right:
                left.append(node.val)
            if node.left:
                add_left(node.left)
            else:
                add_left(node.right)

        def add_right(node):
            if not node:
                return
            if node.left or node.right:
                right.append(node.val)
            if node.right:
                add_right(node.right)
            else:
                add_right(node.left)

        def add_leaves(node):
            if not node:
                return
            if not node.left and not node.right:
                leaves.append(node.val)
            add_leaves(node.left)
            add_leaves(node.right)

        if root.left:
            add_left(root.left)
        if root.right:
            add_right(root.right)
        if root.left or root.right:
            add_leaves(root)
        return [root.val] + left + leaves + right[::-1]


solution = Solution()
solution.boundaryOfBinaryTree(None)
