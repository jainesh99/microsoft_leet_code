import math
from collections import defaultdict


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = [1, n]
        factors_dict = defaultdict(int)

        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                divisor = int(n / i)
                factors_dict[i] = divisor
                factors_dict[divisor] = i
                factors.append(i)

                if i != divisor:
                    factors.append(divisor)

        factors = sorted(factors)

        if k > len(factors):
            return -1
        else:
            return factors[k - 1]


solution = Solution()
n, k = 12, 3
print(solution.kthFactor(n, k))
