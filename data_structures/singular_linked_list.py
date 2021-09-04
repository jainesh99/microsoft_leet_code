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

        if not self.head:
            return None

        if self.head.next:
            temp = self.head.data
            self.head = self.head.next
            self.current_size -= 1
            return temp
        else:
            self.head = None
            self.current_size = 0
            return None

    def remove_last(self):

        if not self.head:
            return None

        if self.head.next:
            previous = None
            current = self.head

            while current.next:
                previous = current
                current = current.next

            previous.next = None
            self.current_size -= 1

            return current.data
        else:
            self.head = None
            self.current_size = 0
            return None

    def remove(self, value):

        if not self.head:
            return None

        if value == self.head.data:
            return self.remove_first()

        previous = None
        current = self.head

        while current and current.data != value:
            previous = current
            current = current.next

        if current:
            previous.next = current.next
            self.current_size -= 1

    def find(self, value):

        if not self.head:
            return False

        if value == self.head.data:
            return True

        current = self.head

        while current:
            if value == current.data:
                return True
            current = current.next

        return False

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
l.add_last(n3)
l.print()
print(l.find(3))
