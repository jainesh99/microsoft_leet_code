from typing import List


class Solution:
    def coinChange(self, coins, amount):
        def coinChangeInner(rem, cache):
            if rem < 0:
                return float("inf")
            if rem == 0:
                return 0
            if rem in cache:
                return cache[rem]

            cache[rem] = min(coinChangeInner(rem - coin, cache) + 1 for coin in coins)
            return cache[rem]

        ans = coinChangeInner(amount, {})
        return -1 if ans == float("inf") else ans


coins = [2]
amount = 3
solution = Solution()
print(solution.coinChange(coins, amount))
