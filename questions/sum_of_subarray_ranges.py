from heapq import heapify, heappush
from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:

        # sum_array_ranges = max(nums) - min(nums)
        #
        # for step in range(2, len(nums)):
        #
        #     for j in range(0, len(nums)):
        #
        #         sub_array = nums[j:j+step]
        #
        #         if len(sub_array) == step:
        #             sum_array_ranges += (max(sub_array) - min(sub_array))
        #
        # return sum_array_ranges

        sum_array_ranges = 0

        for i in range(len(nums)):

            min_heap, max_heap = [], []
            heappush(min_heap, nums[i])
            heappush(max_heap, -nums[i])

            for j in range(i + 1, len(nums)):

                heappush(min_heap, nums[j])
                heappush(max_heap, -nums[j])

                sum_array_ranges += -max_heap[0] - min_heap[0]

        return sum_array_ranges


solution = Solution()
nums = [1, 2, 3]
print(solution.subArrayRanges(nums))
