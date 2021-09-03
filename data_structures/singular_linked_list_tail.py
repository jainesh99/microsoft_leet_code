class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_size = 0

    def add_first(self, value):

        value.next = self.head
        self.head = value

        if not self.head.next:
            self.tail = value

        self.current_size += 1

    def add_last(self, value):

        if self.tail:
            self.tail.next = value
            self.tail = value
            self.current_size += 1
        else:
            self.head = value
            self.tail = value

    def remove_first(self):

        if self.head == self.tail:
            self.head = self.tail = None
            self.current_size = 0
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            self.current_size -= 1
            return temp

    def remove_last(self):

        if self.head == self.tail:
            self.head = self.tail = None
            # Can also just return remove_first() has the same effect
            return None
        else:
            previous = None
            current = self.head

            while current.next:
                previous = current
                current = current.next

            temp = current.data
            previous.next = None
            self.tail = previous
            self.current_size -= 1
            return temp

    def print(self):
        temp = self.head

        print("Start-----------")
        while temp:
            print(temp.data)
            temp = temp.next
        print("End-----------")
        print()


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

l = LinkedList()
l.head = None
l.add_first(n1)
l.add_last(n2)
l.print()
l.remove_last()
l.print()
