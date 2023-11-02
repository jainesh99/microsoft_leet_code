class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_array = nums[0]
        current_sum = 0

        for num in nums:
            if current_sum < 0:
                current_sum = 0

            current_sum += num
            max_array = max(current_sum, max_array)

        return max_array
