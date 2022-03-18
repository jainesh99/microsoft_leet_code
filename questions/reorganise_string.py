from collections import Counter
from queue import PriorityQueue


class Solution:
    def reorganizeString(self, s: str) -> str:

        if not s:
            return ""

        counter = Counter(s)
        priority_queue = PriorityQueue()
        reorganised_string = ""

        for character, count in counter.items():
            priority_queue.put((-count, character))

        count, character = priority_queue.get()
        reorganised_string = reorganised_string + character
        block = (count + 1, character)

        while priority_queue.qsize() > 0:

            count, character = priority_queue.get()
            reorganised_string = reorganised_string + character

            if block[0] < 0:
                priority_queue.put(block)
            block = (count + 1, character)

        if len(reorganised_string) != len(s):
            return ""
        else:
            return reorganised_string


solution = Solution()
s = "vvvlo"
print(solution.reorganizeString(s))
