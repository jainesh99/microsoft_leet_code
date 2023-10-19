from typing import Dict


class Solution:
    def climbStairs(self, n: int, memo: Dict = None) -> int:

        count = 0

        if memo is None:
            memo = {}

        if n == 0 or n == 1:
            return 1

        if n < 0:
            memo[n] = 0
            return 0

        if n not in memo.keys():
            memo[n] = self.climbStairs(n - 1, memo) + self.climbStairs(n - 2, memo)

        return memo[n]


solution = Solution()
print(solution.climbStairs(2))
