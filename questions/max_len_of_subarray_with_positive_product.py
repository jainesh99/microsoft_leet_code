from typing import List

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:

        # if len(nums) == 1:
        #     if nums[0] > 0:
        #         return 1
        #     else:
        #         return 0
        #
        # total_product = 1
        # max_subarray = 0
        # max_length = 0
        #
        # for index, num in enumerate(nums):
        #
        #     if num == 0:
        #         if max_subarray > max_length:
        #             max_length = max_subarray
        #
        #         max_subarray = 1
        #         total_product = 1
        #     else:
        #         total_product = total_product * num
        #
        #         if total_product > 0:
        #             max_subarray += 1
        #
        # if max_subarray > max_length:
        #     max_length = max_subarray
        #
        # return max_length

        first_negative_index = -1
        zero_index = -1
        number_of_negative_values = 0
        max_length = 0

        for index, num in enumerate(nums):

            if num < 0:
                number_of_negative_values += 1

                if first_negative_index == -1:
                    first_negative_index = index

            if num == 0:
                number_of_negative_values = 0
                first_negative_index = -1
                zero_index = index
            else:
                if number_of_negative_values % 2 == 0:
                    max_length = max(index - zero_index, max_length)
                else:
                    max_length = max(index - first_negative_index, max_length)

        return max_length


solution = Solution()
nums = [0,1,-2,-3,-4]
print(solution.getMaxLen(nums))