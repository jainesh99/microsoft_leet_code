from collections import defaultdict
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        pairs = {}
        count = 0
        for i in time:
            r = i % 60
            if (60 - r) in pairs:
                count = count + pairs[(60 - r)]
            if r == 0 and r in pairs:
                count = count + pairs[r]
            if r in pairs:
                pairs[r] += 1
            else:
                pairs[r] = 1
        return count


solution = Solution()
time = [60, 60, 60]
solution.numPairsDivisibleBy60(time)
