class Node:

    def __init__(self, data):
        self.data = data
        self.left, self.right = None, None


class Tree:

    def __init__(self):
        self._root = None

    def add(self, data):

        if not self._root:
            self._root = Node(data)
        else:
            self._add(data, self._root)

    def _add(self, data, node):

        if data > node.data:

            if not node.right:
                node.right = Node(data)
            else:
                self._add(data, node.right)
        else:

            if not node.left:
                node.left = Node(data)
            else:
                self._add(data, node.left)

    # def print_tree(self):
    #     # Level order traversal


temp_tree = Tree()
temp_tree.add(10)
temp_tree.add(6)
temp_tree.add(15)
temp_tree.add(4)
temp_tree.add(7)

print("Done")