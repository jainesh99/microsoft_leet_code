import math
from collections import defaultdict, deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#
#         level_order_queue = deque()
#         level_order_queue.append(root)
#
#         zig_zag_order_dict = defaultdict(list)
#         zig_zag_order_list = []
#         level = 0
#         counter = 0
#         left_to_right = False
#
#         while level_order_queue:
#
#             node = level_order_queue.popleft()
#             counter += 1
#
#             if node:
#                 if left_to_right:
#                     zig_zag_order_dict[level].append(node.val)
#                 else:
#                     zig_zag_order_dict[level].insert(0, node.val)
#
#                 left_node = node.left
#                 right_node = node.right
#
#                 level_order_queue.append(left_node)
#                 level_order_queue.append(right_node)
#
#             if level ** 2 == counter:
#                 counter = 0
#                 level += 1
#
#         for item, value in zig_zag_order_dict.items():
#             zig_zag_order_list.append(value)
#
#         return zig_zag_order_list
#
class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        level_list = deque()
        if root is None:
            return []
        # start with the level 0 with a delimiter
        node_queue = deque([root, None])
        is_order_left = True

        while node_queue:
            curr_node = node_queue.popleft()

            if curr_node:
                if is_order_left:
                    level_list.append(curr_node.val)
                else:
                    level_list.appendleft(curr_node.val)

                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)
            else:
                # we finish one level
                ret.append(level_list)
                # add a delimiter to mark the level
                if len(node_queue) > 0:
                    node_queue.append(None)

                # prepare for the next level
                level_list = deque()
                is_order_left = not is_order_left

        return ret


solution = Solution()
root = [3, 9, 20, None, None, 15, 7]
solution.zigzagLevelOrder(root)
