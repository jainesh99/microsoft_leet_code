from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        nums_set = set(nums)

        for num in nums:

            if num - 1 not in nums_set:
                current_streak = 1
                current_num = num

                while current_num + 1 in nums_set:
                    current_streak += 1
                    current_num = current_num + 1

                longest_streak = max(current_streak, longest_streak)

        return longest_streak


solution = Solution()
nums = [100, 4, 200, 1, 3, 2]
solution.longestConsecutive(nums)
