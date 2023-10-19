from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        items = {value for value in range(len(nums) + 1)}
        nums_set = set(nums)

        return list(items - nums_set)[0]


solution = Solution()
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(solution.missingNumber(nums))
