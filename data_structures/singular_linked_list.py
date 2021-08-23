class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.current_size = 0

    def add_first(self, value):

        value.next = self.head
        self.head = value

        self.current_size += 1

    def add_last(self, value):
        temp = self.head

        if temp:
            while temp.next:
                temp = temp.next

            temp.next = value
            self.current_size += 1
        else:
            self.head = value
            self.current_size += 1
            # OR can call the self.add_first(value)

    def print(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

l = LinkedList()
l.head = None
l.add_last(n1)
l.print()
