from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:

        product = 1

        for num in nums:
            if num == 0:
                return 0
            product = product * num

        if product > 0:
            return 1
        else:
            return -1


solution = Solution()
print(solution.arraySign([1, 2, 0, 4, 5]))
