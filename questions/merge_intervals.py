from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort()
        result = [intervals[0]]

        for start, end in intervals[1:]:
            prev_start = result[-1][0]
            prev_end = result[-1][1]
            if (start <= prev_end) and (start >= prev_start):
                result[-1][1] = max(prev_end, end)
            else:
                result.append([start, end])

        return result


solution = Solution()
intervals = [[9, 10], [10, 11], [8, 10], [15, 18]]
solution.merge(intervals)
