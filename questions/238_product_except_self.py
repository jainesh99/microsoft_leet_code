from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right, result = [1] * len(nums), [1] * len(nums), [1] * len(nums)

        for index in range(1, len(nums)):
            left[index] = nums[index - 1] * left[index - 1]

        for index in range(len(nums) - 1, 0, -1):
            right[index - 1] = nums[index] * right[index]

        result = [left[index] * right[index] for index in range(len(nums))]

        return result


nums = [-1, 1, 0, -3, 3]
solution = Solution()
print(solution.productExceptSelf(nums))
