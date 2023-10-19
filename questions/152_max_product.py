from typing import List


class Solution:
    def maxProduct_brute_force(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        max_product = 1

        for num in nums:
            max_product = max_product * num

        max_product = max(max_product, max(nums))

        for index in range(len(nums)):
            new_max_product = nums[index]

            for new_index in range(index + 1, len(nums)):

                new_max_product = new_max_product * nums[new_index]

                if new_max_product > max_product:
                    max_product = new_max_product

        return max_product

    def maxProduct(self, nums):
        res = max(nums)
        cur_min, cur_max = 1, 1

        for n in nums:
            tmp = cur_max * n
            cur_max = max(n * cur_max, n * cur_min, n)
            cur_min = min(tmp, n * cur_min, n)
            res = max(res, cur_max)

        return res


solution = Solution()
print(solution.maxProduct([2, -5, -2, -4, 3]))
