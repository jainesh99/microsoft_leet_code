from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        cost = 0

        # while len(sticks) > 1:
        #     sticks = sorted(sticks)
        #     first_val = sticks.pop(0)
        #     second_val = sticks.pop(0)
        #     cost = cost + first_val + second_val
        #     sticks.append(first_val + second_val)

        # Heap
        heapify(sticks)

        while len(sticks) > 1:
            value_to_add = heappop(sticks) + heappop(sticks)
            cost = cost + value_to_add
            heappush(sticks, value_to_add)

        return cost


solution = Solution()
sticks = [2, 4, 3]
print(solution.connectSticks(sticks))
