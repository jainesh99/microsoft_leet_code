from heapq import heapify, heappop
from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        :type arr: List[int]
        :rtype: int
        """
        su = 0
        arr.append(0)
        stack = [-1]
        for i, num in enumerate(arr):
            # maintain an non-decreasing stack
            while stack and arr[stack[-1]] > num:  # (i)
                idx = stack.pop()
                su += arr[idx] * (i - idx) * (idx - stack[-1])
            stack.append(i)
        return su % (10**9 + 7)


solution = Solution()
arr = [3, 1, 2, 4]
print(solution.sumSubarrayMins(arr))
