from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        def sf(a, b):
            return (a * (a + 1) - b * (b + 1)) // 2

        inventory.sort(reverse=True)  # Use a heap also could work better
        inventory.append(0)
        total, index, repeats = 0, 0, 0

        while orders > 0:
            repeats += 1
            n = (inventory[index] - inventory[index + 1]) * repeats
            if orders >= n:  # Simple case
                s = sf(inventory[index], inventory[index + 1])
                total += repeats * s
                orders -= n
            else:
                r = orders % repeats  # Last remainder row
                c = (orders - r) // repeats  # Fully filled columns
                s = sf(inventory[index], inventory[index] - c)
                total += repeats * s + (inventory[index] - c) * r
                return total % (10 ** 9 + 7)
            index += 1

        return total % (10 ** 9 + 7)

        # def get_natural_number_sum(start, end):
        #
        #     if end < 0:
        #         end = 0
        #
        #     return (start * (start + 1) - end * (end + 1))//2
        #
        # if len(inventory) == 1:
        #     return (get_natural_number_sum(inventory[0], inventory[0] - orders)) % (10**9 + 7)
        #
        # inventory = [i * -1 for i in inventory]
        # heapify(inventory)
        # profit = 0
        #
        # while orders > 0:
        #     value = heappop(inventory)*-1
        #     profit = profit + value
        #     orders -= 1
        #     value -= 1
        #     heappush(inventory, value*-1)
        #
        # return profit % (10 ** 9 + 7)


solution = Solution()
inventory = [3, 5]
orders = 6
print(solution.maxProfit(inventory, orders))
