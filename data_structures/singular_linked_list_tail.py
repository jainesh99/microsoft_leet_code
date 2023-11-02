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

            while current.next:  # Can also do while current != tail
                previous = current
                current = current.next

            previous.next = None
            self.tail = previous
            self.current_size -= 1
            return current.data

    def remove(self, value):
        if not self.head:
            return None

        if value == self.head.data:
            return self.remove_first()

        if value == self.tail.data:
            return self.remove_last()

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

        if value == self.tail.data:
            return True

        current = self.head

        while current:
            if value == current.data:
                return True
            current = current.next

        return False

    def peak_first(self):
        if self.head:
            return self.head.data
        else:
            return None

    def peak_last(self):
        if self.tail:
            return self.tail.data
        else:
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
l.head = None
l.add_first(n1)
l.add_last(n2)
l.add_last(n3)
l.print()
print(l.peak_last())
