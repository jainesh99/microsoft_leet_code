import math


class Heap:

    def __init__(self):
        self._last_position = 0
        self._arr_heap = []

    def add(self, value):

        if len(self._arr_heap) == 0:
            self._arr_heap.append(value)
        else:
            self._last_position += 1
            self._arr_heap.append(value)
            self.trickle_up()

    def trickle_up(self):

        parent_index = math.floor((self._last_position-1)/2)
        child_index = self._last_position

        while self._arr_heap[parent_index] < self._arr_heap[child_index]:
            parent_value = self._arr_heap[parent_index]
            child_value = self._arr_heap[child_index]

            self._arr_heap[child_index] = parent_value
            self._arr_heap[parent_index] = child_value

            child_index = parent_index
            parent_index = math.floor((child_index-1)/2)

            if parent_index < 0:
                parent_index = 0


h = Heap()
h.add(5)
h.add(50)
h.add(100)
print("Complete")
