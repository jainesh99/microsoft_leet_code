from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        current_min = prices[0]
        max_profit = 0

        for index in range(1,len(prices)):

            price = prices[index]

            if price < current_min:
                current_min = price
            else:
                if price - current_min > max_profit:
                    max_profit = price - current_min

        return max_profit






prices = [7,6,4,3,1]
solution = Solution()
print(solution.maxProfit(prices))