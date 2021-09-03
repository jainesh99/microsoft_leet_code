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

    def remove_first(self):

        if self.head.next:
            temp = self.head.data
            self.head = self.head.next
            self.current_size -= 1
            return temp
        else:
            self.head = None
            return None

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
l.add_first(n1)
l.add_first(n2)
l.print()
l.remove_first()
l.print()
