import abc
from abc import ABC, abstractmethod
from typing import List

"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""


class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass


class TreeNode(Node):
    def evaluate(self):
        if self.value.isdigit():
            return int(self.value)
        elif self.value == "*":
            return self.left.evaluate() * self.right.evaluate()
        elif self.value == "+":
            return self.left.evaluate() + self.right.evaluate()
        elif self.value == "-":
            return self.left.evaluate() - self.right.evaluate()
        else:
            return self.left.evaluate() // self.right.evaluate()

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""


class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> "Node":
        root, stack = None, []
        for item in postfix:
            if item.isdigit():
                root = TreeNode(item)
            else:
                root = TreeNode(item)
                root.right = stack.pop()
                root.left = stack.pop()
            stack.append(root)
        return root


"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""

obj = TreeBuilder()
postfix = ["4", "5", "2", "7", "+", "-", "*"]
expTree = obj.buildTree(postfix)
ans = expTree.evaluate()
print(ans)
