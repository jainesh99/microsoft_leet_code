from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for index, x in enumerate(nums):
            if index > 0 and x == nums[index - 1]:
                continue

            left, right = index + 1, len(nums) - 1

            while left < right:
                three_sum = x + nums[left] + nums[right]

                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    res.append([x, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return res


solution = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(solution.threeSum(nums))
