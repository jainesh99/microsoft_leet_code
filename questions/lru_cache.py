from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self._cache:
            self._cache.move_to_end(key)
            return self._cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self._cache[key] = value
        self._cache.move_to_end(
            key
        )  # This may be because you are adding a new one, so it may be given a chance to get called
        if len(self._cache) > self._capacity:
            self._cache.popitem(last=False)


response = [None]

operations = ["LRUCache", "put", "put", "put", "put", "get", "get"]
values = [[2], [2, 1], [1, 1], [2, 3], [4, 1], [1], [2]]

lRUCache = LRUCache(values[0][0])

for index in range(1, len(operations)):
    item = values[index]

    if operations[index] == "put":
        response.append(lRUCache.put(item[0], item[1]))
    elif operations[index] == "get":
        response.append(lRUCache.get(item[0]))

print(response)
