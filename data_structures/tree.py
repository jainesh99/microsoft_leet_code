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

    def contains(self, data):
        if self._root:
            response = self._contains(data, self._root)
            if response:
                return True
            else:
                return False
        else:
            return False

    def _contains(self, data, node):
        if not node:
            return False
        elif data == node.data:
            return True
        elif data > node.data:
            return self._contains(data, node.right)
        else:
            return self._contains(data, node.left)

    # def print_tree(self):
    #     # Level order traversal

    def remove(self, data):
        self._remove(data, self._root)

    def _remove(self, data, node):
        if node is None:
            return node

        if data < node.data:
            node.left = self._remove(data, node.left)
        elif data > node.data:
            node.right = self._remove(data, node.right)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp


temp_tree = Tree()
temp_tree.add(10)
temp_tree.add(6)
temp_tree.add(15)
temp_tree.add(4)
temp_tree.add(7)

print(temp_tree.contains(7))

print("Done")
