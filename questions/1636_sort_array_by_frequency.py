from collections import defaultdict
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency_map = defaultdict(int)

        for num in nums:
            frequency_map[num] += 1

        return sorted(nums, key=lambda x: (frequency_map[x], -x))


solution = Solution()
nums = [2, 3, 1, 3, 2]
print(solution.frequencySort(nums))
