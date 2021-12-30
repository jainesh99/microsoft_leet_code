# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        stack = []
        num_of_good_nodes = 0

        stack.append((root, root.val))

        while len(stack) > 0:

            popped_node, max_value_so_far = stack.pop()

            if popped_node.val >= max_value_so_far:
                num_of_good_nodes += 1
                max_value_so_far = popped_node.val

            if popped_node.right:
                stack.append((popped_node.right, max_value_so_far))

            if popped_node.left:
                stack.append((popped_node.left, max_value_so_far))

        return num_of_good_nodes
